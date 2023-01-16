""" SCADA Actor """
import functools
import logging
import random
import time
from abc import abstractmethod
from typing import Optional
from typing import no_type_check

import gridworks.algo_utils as algo_utils
import pendulum
from algosdk.atomic_transaction_composer import TransactionWithSigner
from algosdk.future.transaction import *
from algosdk.v2client.algod import AlgodClient
from beaker.client import ApplicationClient
from gridworks.actor_base import ActorBase
from gridworks.algo_utils import BasicAccount
from gridworks.message import as_enum
from gwproto.messages import GtShStatus_Maker
from gwproto.messages import GtTelemetry_Maker
from gwproto.messages import SnapshotSpaceheat_Maker

from gwatn import DispatchContract
from gwatn.config import ScadaSettings
from gwatn.enums import GNodeRole
from gwatn.enums import MessageCategorySymbol
from gwatn.enums import UniverseType
from gwatn.types import GtDispatchBoolean
from gwatn.types import GtDispatchBoolean_Maker
from gwatn.types import HeartbeatA
from gwatn.types import HeartbeatA_Maker
from gwatn.types import HeartbeatAlgoAudit
from gwatn.types import HeartbeatAlgoAudit_Maker
from gwatn.types import HeartbeatB
from gwatn.types import HeartbeatB_Maker
from gwatn.types import SimTimestep
from gwatn.types import SimTimestep_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(sasctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)


class ScadaActor(ActorBase):
    def __init__(self, settings: ScadaSettings):
        super().__init__(settings=settings)
        self.settings: ScadaSettings = settings
        self.acct: BasicAccount = BasicAccount(settings.sk.get_secret_value())
        self.client: AlgodClient = AlgodClient(
            settings.algo_api_secrets.algod_token.get_secret_value(),
            settings.public.algod_address,
        )
        # The dc_client (DispatchContract client) builds on top of the Algorand beaker ApplicationClient
        self.dc_client = ApplicationClient(
            self.client, DispatchContract(), signer=self.acct.as_signer()
        )
        self.scada_cert_id: Optional[int] = None
        self.dc_app_id: Optional[int] = None
        self.universe_type = as_enum(
            self.settings.universe_type_value, UniverseType, UniverseType.default()
        )
        self._time: float = self.get_initial_time_s()
        self.atn_gni_id: Optional[int] = None
        self.atn_addr: Optional[str] = None

    def check_dispatch_contract_on_init(self):
        """The dispatch contract may already exist. If it does, populate the relevant
        attributes"""
        app_ids = (
            self.client.account_info(self.acct.addr).get("apps-total-schema", []).keys()
        )

        self.client.account_info(self.acct.addr)

    @property
    def atn_alias(self):
        """Removes `ta.scada` from the end of the SCADA's GNodeAlias"""
        return self.alias[:-9]

    @property
    def ta_alias(self):
        """Removes `ta.scada` from the end of the SCADA's GNodeAlias"""
        return self.alias[:-3]

    def local_rabbit_startup(self) -> None:
        rjb = MessageCategorySymbol.rjb.value
        tc_alias_lrh = self.settings.time_coordinator_alias.replace(".", "-")
        binding = f"{rjb}.{tc_alias_lrh}.timecoordinator.sim-timestep"

        cb = functools.partial(self.on_timecoordinator_bindok, binding=binding)
        self._consume_channel.queue_bind(
            self.queue_name, "timecoordinatormic_tx", routing_key=binding, callback=cb
        )
        LOGGER.info(
            f"Queue {self.queue_name} bound to timecoordinatormic_tx with {binding} "
        )

    @no_type_check
    def on_timecoordinator_bindok(self, _unused_frame, binding) -> None:
        LOGGER.info(f"Queue {self.queue_name} bound with {binding}")

    def time(self) -> float:
        if self.universe_type == UniverseType.Dev:
            return self._time
        else:
            return time.time()

    def get_initial_time_s(self) -> float:
        if self.universe_type == UniverseType.Dev:
            return self.settings.initial_time_unix_s
        else:
            return time.time()

    def prepare_for_death(self) -> None:
        self.actor_main_stopped = True

    ########################
    ## Receives
    ########################

    def route_message(
        self, from_alias: str, from_role: GNodeRole, payload: HeartbeatB
    ) -> None:
        if payload.TypeName == GtDispatchBoolean_Maker.type_name:
            if from_role != GNodeRole.AtomicTNode:
                LOGGER.info(
                    f"Ignoring GtDispatchBooleanfrom GNode with role {from_role}; expects AtomicTNode"
                )
            try:
                self.dispatch_received(payload)
            except:
                LOGGER.exception("Error in dispatch_received")

        elif payload.TypeName == HeartbeatA_Maker.type_name:
            if from_role != GNodeRole.Supervisor:
                LOGGER.info(
                    f"Ignoring HeartbeatB from GNode with role {from_role}; expects Supervisor"
                )
            try:
                self.heartbeat_from_super(payload)
            except:
                LOGGER.exception("Error in heartbeat_from_super")
        elif payload.TypeName == HeartbeatB_Maker.type_name:
            if from_role != GNodeRole.AtomicTNode:
                LOGGER.info(
                    f"Ignoring HeartbeatB from GNode with role {from_role}; expects AtomicTNode"
                )
            try:
                self.heartbeat_from_partner(payload)
            except:
                LOGGER.exception("Error in heartbeat_from_partner")
        elif payload.TypeName == SimTimestep_Maker.type_name:
            if from_role != GNodeRole.TimeCoordinator:
                LOGGER.info(
                    f"Ignoring HeartbeatB from GNode with role {from_role}; expects TimeCoordinator"
                )
            try:
                self.timestep_from_timecoordinator(payload)
            except:
                LOGGER.exception("Error in timestep_from_timecoordinator")

    def heartbeat_from_partner(self, ping: HeartbeatB) -> None:
        """
        This is the Scada's half of the DispatchContract Heartbeat pattern.
        It:
          - Checks that it has a DispatchContract (owns that SmartContract)
          - Checks the GNodeAlias and GNodeInstanceId to validate partner
          - Sends a reply HeartbeatB immediately back using a RabbitJsonDirect message
          - Sends an audit report of its action to the DispatchContract
            # TODO: save audit report for sending in a batch if SmartContract
            # exists but is not reachable (i.e. blockchain down)
        [more info](https://gridworks.readthedocs.io/en/latest/dispatch-contract.html)

        Args:
            payload (HeartbeatB): The latest heartbeat received from its
            AtomicTNode partner

        """
        ...

    def heartbeat_from_super(self, from_alias: str, ping: HeartbeatA) -> None:
        pong = HeartbeatA_Maker(
            my_hex=str(random.choice("0123456789abcdef")), your_last_hex=ping.MyHex
        ).tuple

        self.send_message(
            payload=pong,
            to_role=GNodeRole.Supervisor,
            to_g_node_alias=self.settings.my_super_alias,
        )

        LOGGER.debug(
            f"[{self.alias}] Sent HB: SuHex {pong.YourLastHex}, AtnHex {pong.MyHex}"
        )

    def timestep_from_timecoordinator(self, payload: SimTimestep):
        if self._time == 0:
            self._time = payload.TimeUnixS
            self.new_timestep(payload)
            LOGGER.info(f"TIME STARTED: {self.time_str()}")
        elif self._time < payload.TimeUnixS:
            self._time = payload.TimeUnixS
            self.new_timestep(payload)
            LOGGER.debug(f"Time is now {self.time_str()}")
        elif self._time == payload.TimeUnixS:
            self.repeat_timestep(payload)

    ########################################################
    #  Related to Dispatch Contract and Scada Cert
    ########################################################

    def initialize_dispatch_contract(self):
        """Starts up Dispatch contract to be used with AtomicTNode.

        Raises exception if Scada Addr
            - has less than 20 Algos
            - already has created an app
            - does not already have a unique Scada Cert ASA
        """
        if algo_utils.algos(self.acct.addr) < 20:
            raise Exception(
                f"Please fund Scada addr with at least 12 Algoss: {self.acct.addr}"
            )
        if len(self.client.account_info(self.acct.addr)["created-apps"]) > 0:
            raise Exception("Please stop entire simulation and reset sandbox")
        balances = algo_utils.get_balances(self.client, self.acct.addr)
        non_algo_asas = list(set(balances.keys()) - {0})
        scada_certs = list(
            filter(
                lambda x: self.client.asset_info(x)["params"]["unit-name"] == "SCADA",
                non_algo_asas,
            )
        )
        if len(scada_certs) > 1:
            raise Exception(
                f"Scada {self.alias} has 2 scada certs. This should not happen!"
            )
        if len(scada_certs) == 0:
            raise Exception(
                "Scada acct needs to be created and funded by TaOwner, and Scada GNode "
                "needs to be authorized (with GNodeFactory sending Scada cert) "
                f"before starting up {self.alias}"
            )

        self.scada_cert_id = scada_certs[0]
        # Start Dispatch contract
        app_id, app_address, transaction_id = self.dc_client.create()
        self.dc_app_id = app_id

        sp = self.dc_client.get_suggested_params()
        sp.flat_fee = True
        sp.fee = 2000
        ptxn = PaymentTxn(self.acct.addr, sp, self.dc_client.app_addr, 14_000_000)

        # Now do the first half of bootstrapping the contract by providing it
        # with enough money to fund about 32kB in boxes, along with
        # our ScadaCertId (which can be shown to match our address in the sig)

        result = self.dc_client.call(
            DispatchContract.bootstrap1,
            scada_seed=TransactionWithSigner(ptxn, self.acct.as_signer()),
            ScadaCert=self.scada_cert_id,
        )

        if result.return_value != self.ta_alias:
            raise Exception(
                f"Expected {self.ta_alias} back from bootstrapping app {self.dc_app_id}, but"
                f" got {result.return_value}"
            )

    #########################################################
    # Below be made abstractmethods if pulling out base class
    #########################################################

    def dispatch_received(payload: GtDispatchBoolean) -> None:
        """
        Dispatch received from AtomicTNode

          - Checks that the GNodeAlias and GNodeInstanceId belong to its
        AtomicTNode
          - Follows instructions (turns on or turns off)

        For hourly sim:
          - Updates energy and power
          - Send status to AtomicTNode
        """
        raise NotImplementedError

    def new_timestep(self, payload: SimTimestep) -> None:
        # LOGGER.info("New timestep in atn_actor_base")
        if self.dc_app_id is None:
            self.initialize_dispatch_contract()

    def repeat_timestep(self, payload: SimTimestep) -> None:
        # LOGGER.info("Timestep received again in atn_actor_base")
        raise NotImplementedError

    def time_str(self) -> str:
        return pendulum.from_timestamp(self.time()).strftime("%m/%d/%Y, %H:%M")

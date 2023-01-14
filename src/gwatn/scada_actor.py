""" SCADA Actor """
import functools
import logging
import random
import time
from abc import abstractmethod
from typing import no_type_check

import pendulum
from gridworks.actor_base import ActorBase
from gridworks.message import as_enum
from gwproto.messages import GtShStatus_Maker
from gwproto.messages import GtTelemetry_Maker
from gwproto.messages import SnapshotSpaceheat_Maker

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


class Scada(ActorBase):
    def __init__(self, settings: ScadaSettings):
        super().__init__(settings=settings)
        self.settings: ScadaSettings = settings
        self.universe_type = as_enum(
            self.settings.universe_type_value, UniverseType, UniverseType.default()
        )
        self._time: float = self.get_initial_time_s()

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
        self.strategy_rabbit_startup()

    def strategy_rabbit_startup(self) -> None:
        pass

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
        if payload.TypeName == HeartbeatA_Maker.type_name:
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
        if payload.TypeName == SimTimestep_Maker.type_name:
            try:
                self.timestep_from_timecoordinator(payload)
            except:
                LOGGER.exception("Error in timestep_from_timecoordinator")
        elif payload.TypeName == GtDispatchBoolean_Maker.type_name:
            if from_role != GNodeRole.AtomicTNode:
                LOGGER.info(
                    f"Ignoring GtDispatchBooleanfrom GNode with role {from_role}; expects AtomicTNode"
                )
            try:
                self.dispatch_received(payload)
            except:
                LOGGER.exception("Error in dispatch_received")

    def heartbeat_from_partner(self, ping: HeartbeatB) -> None:
        """
        This is the Scada's half of the DispatchContract Heartbeat pattern.
        It:
          - Checks that it has a DispatchContract (owns that SmartContract)
          - Checks the GNodeAlias and GNodeInstanceId to validate partner
          - Sends a reply HeartbeatB back using a RabbitJsonDirect message
          - Sends an audit report of its action to the DispatchContract
            # TODO: save audit report for sending in a batch if SmartContract
            # exists but is not reachable (i.e. blockchain down)
        [more info](https://gridworks.readthedocs.io/en/latest/dispatch-contract.html)

        Args:
            payload (HeartbeatB): The latest heartbeat received from its
            AtomicTNode partner

        """

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
        raise NotImplementedError

    def repeat_timestep(self, payload: SimTimestep) -> None:
        # LOGGER.info("Timestep received again in atn_actor_base")
        raise NotImplementedError

    def time_str(self) -> str:
        return pendulum.from_timestamp(self.time()).strftime("%m/%d/%Y, %H:%M")

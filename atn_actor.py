from algosdk.v2client.algod import AlgodClient
from beaker.client import ApplicationClient
from gridworks.algo_utils import BasicAccount

from gwatn import DispatchContract
from gwatn.atn_actor_base import AtnActorBase
from gwatn.config import AtnSettings
from gwatn.types import DispatchContractConfirmed_Maker
from gwatn.types import JoinDispatchContract
from gwatn.types import LatestPrice
from gwatn.types import SimTimestep


class AtnActor(AtnActorBase):
    def __init__(self, settings: AtnSettings):
        super().__init__(settings=settings)
        self.acct: BasicAccount = BasicAccount(settings.sk.get_secret_value())
        self.client: AlgodClient = AlgodClient(
            settings.algo_api_secrets.algod_token.get_secret_value(),
            settings.public.algod_address,
        )
        self.dc_client = ApplicationClient(
            self.client, DispatchContract(), signer=self.acct.as_signer()
        )
        self.has_dispatch_contract: bool = False
        self.talking_with: bool = False
        self.ta_trading_rights_idx: Optional[int] = None
        self.dispatch_contract_app_id: Optional[int] = None

    @property
    def ta_alias(self):
        """Add `ta` to the and of the Atn's GNodeAlias"""
        return self.alias + ".ta"

    @property
    def scada_alias(self):
        """Add `ta.scada` from the end of the Atn's's GNodeAlias"""
        return self.alias + ".ta.scada"

    def join_dispatch_contract_from_scada(self, payload: JoinDispatchContract) -> None:
        raise NotImplementedError

    def latest_price_from_market_maker(self, payload: LatestPrice) -> None:
        pass

    def new_timestep(self, payload: SimTimestep) -> None:
        pass

    def repeat_timestep(self, payload: SimTimestep) -> None:
        pass

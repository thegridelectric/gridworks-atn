""" List of all the types used"""
from typing import Dict
from typing import List
from typing import no_type_check

from gwatn.types import AcceptedBid_Maker
from gwatn.types import AtnBid_Maker
from gwatn.types import AtnParams_Maker
from gwatn.types import AtnParamsBrickstorageheater_Maker
from gwatn.types import AtnParamsReport_Maker
from gwatn.types import BasegnodeScadaCreate_Maker
from gwatn.types import DiscoverycertAlgoCreate_Maker
from gwatn.types import DispatchContractConfirmed_Maker
from gwatn.types import FloParams_Maker
from gwatn.types import FloParamsBrickstorageheater_Maker
from gwatn.types import FloParamsReport_Maker
from gwatn.types import GtDispatchBoolean_Maker
from gwatn.types import HeartbeatB_Maker
from gwatn.types import InitialTadeedAlgoCreate_Maker
from gwatn.types import InitialTadeedAlgoOptin_Maker
from gwatn.types import InitialTadeedAlgoTransfer_Maker
from gwatn.types import JoinDispatchContract_Maker
from gwatn.types import LatestPrice_Maker
from gwatn.types import MarketSlot_Maker
from gwatn.types import MarketTypeGt_Maker
from gwatn.types import NewTadeedAlgoOptin_Maker
from gwatn.types import NewTadeedSend_Maker
from gwatn.types import OldTadeedAlgoReturn_Maker
from gwatn.types import PriceQuantity_Maker
from gwatn.types import PriceQuantityUnitless_Maker
from gwatn.types import ScadaCertTransfer_Maker
from gwatn.types import SimplesimDriverData_Maker
from gwatn.types import SimplesimDriverDataBsh_Maker
from gwatn.types import SimplesimDriverReport_Maker
from gwatn.types import SimplesimSnapshotBrickstorageheater_Maker
from gwatn.types import SlaEnter_Maker
from gwatn.types import TadeedSpecsHack_Maker
from gwatn.types import TavalidatorcertAlgoCreate_Maker
from gwatn.types import TavalidatorcertAlgoTransfer_Maker
from gwatn.types import TerminalassetCertifyHack_Maker


TypeMakerByName: Dict[str, HeartbeatA_Maker] = {}


@no_type_check
def type_makers() -> List[HeartbeatA_Maker]:
    return [
        AcceptedBid_Maker,
        AtnBid_Maker,
        AtnParams_Maker,
        AtnParamsBrickstorageheater_Maker,
        AtnParamsReport_Maker,
        BasegnodeScadaCreate_Maker,
        DiscoverycertAlgoCreate_Maker,
        DispatchContractConfirmed_Maker,
        FloParams_Maker,
        FloParamsBrickstorageheater_Maker,
        FloParamsReport_Maker,
        GtDispatchBoolean_Maker,
        HeartbeatB_Maker,
        InitialTadeedAlgoCreate_Maker,
        InitialTadeedAlgoOptin_Maker,
        InitialTadeedAlgoTransfer_Maker,
        JoinDispatchContract_Maker,
        LatestPrice_Maker,
        MarketSlot_Maker,
        MarketTypeGt_Maker,
        NewTadeedAlgoOptin_Maker,
        NewTadeedSend_Maker,
        OldTadeedAlgoReturn_Maker,
        PriceQuantity_Maker,
        PriceQuantityUnitless_Maker,
        ScadaCertTransfer_Maker,
        SimplesimDriverData_Maker,
        SimplesimDriverDataBsh_Maker,
        SimplesimDriverReport_Maker,
        SimplesimSnapshotBrickstorageheater_Maker,
        SlaEnter_Maker,
        TadeedSpecsHack_Maker,
        TavalidatorcertAlgoCreate_Maker,
        TavalidatorcertAlgoTransfer_Maker,
        TerminalassetCertifyHack_Maker,
    ]


for maker in type_makers():
    TypeMakerByName[maker.type_name] = maker


def version_by_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are TypeNames, values are versions
    """

    v: Dict[str, str] = {
        "accepted.bid": "000",
        "atn.bid": "001",
        "atn.params": "000",
        "atn.params.brickstorageheater": "000",
        "atn.params.report": "000",
        "basegnode.scada.create": "000",
        "discoverycert.algo.create": "000",
        "dispatch.contract.confirmed": "000",
        "flo.params": "000",
        "flo.params.brickstorageheater": "000",
        "flo.params.report": "000",
        "gt.dispatch.boolean": "110",
        "heartbeat.b": "001",
        "initial.tadeed.algo.create": "000",
        "initial.tadeed.algo.optin": "002",
        "initial.tadeed.algo.transfer": "000",
        "join.dispatch.contract": "000",
        "latest.price": "000",
        "market.slot": "000",
        "market.type.gt": "000",
        "new.tadeed.algo.optin": "000",
        "new.tadeed.send": "000",
        "old.tadeed.algo.return": "000",
        "price.quantity": "000",
        "price.quantity.unitless": "000",
        "scada.cert.transfer": "000",
        "simplesim.driver.data": "000",
        "simplesim.driver.data.bsh": "000",
        "simplesim.driver.report": "000",
        "simplesim.snapshot.brickstorageheater": "000",
        "sla.enter": "000",
        "tadeed.specs.hack": "000",
        "tavalidatorcert.algo.create": "000",
        "tavalidatorcert.algo.transfer": "000",
        "terminalasset.certify.hack": "000",
    }

    return v


def status_by_versioned_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are versioned TypeNames, values are type status
    """

    v: Dict[str, str] = {
        "accepted.bid.000": "Pending",
        "atn.bid.001": "Pending",
        "atn.params.000": "Active",
        "atn.params.brickstorageheater.000": "Active",
        "atn.params.report.000": "Active",
        "basegnode.scada.create.000": "Active",
        "discoverycert.algo.create.000": "Active",
        "dispatch.contract.confirmed.000": "Active",
        "flo.params.000": "Pending",
        "flo.params.brickstorageheater.000": "Pending",
        "flo.params.report.000": "Pending",
        "gt.dispatch.boolean.110": "Active",
        "heartbeat.b.001": "Active",
        "initial.tadeed.algo.create.000": "Active",
        "initial.tadeed.algo.optin.002": "Active",
        "initial.tadeed.algo.transfer.000": "Active",
        "join.dispatch.contract.000": "Active",
        "latest.price.000": "Pending",
        "market.slot.000": "Pending",
        "market.type.gt.000": "Pending",
        "new.tadeed.algo.optin.000": "Active",
        "new.tadeed.send.000": "Active",
        "old.tadeed.algo.return.000": "Active",
        "price.quantity.000": "Pending",
        "price.quantity.unitless.000": "Pending",
        "scada.cert.transfer.000": "Pending",
        "simplesim.driver.data.000": "Pending",
        "simplesim.driver.data.bsh.000": "Pending",
        "simplesim.driver.report.000": "Pending",
        "simplesim.snapshot.brickstorageheater.000": "Pending",
        "sla.enter.000": "Pending",
        "tadeed.specs.hack.000": "Pending",
        "tavalidatorcert.algo.create.000": "Active",
        "tavalidatorcert.algo.transfer.000": "Active",
        "terminalasset.certify.hack.000": "Pending",
    }

    return v

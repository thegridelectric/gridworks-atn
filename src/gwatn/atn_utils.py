from typing import List
from typing import Optional

from pydantic import BaseModel

from gwatn import property_format
from gwatn.data_classes import MarketType
from gwatn.strategies.heatpumpwithbooststore.flo import (
    HeatPumpWithBoostStore__Flo as Flo,
)
from gwatn.types import AtnBid
from gwatn.types import AtnParams
from gwatn.types import FloParamsHeatpumpwithbooststore as FloParams
from gwatn.types import FloParamsHeatpumpwithbooststore_Maker as FloParams_Maker
from gwatn.types import MarketSlot
from gwatn.types import MarketTypeGt_Maker
from gwatn.types import PriceQuantityUnitless


DUMMY_ALGO_TXN = "gqNzaWfEQNPXbrAiWd+cNgsIaM3N0PSu3repauvmjuHmoKjh6sd3L5U4/YpovcXN7/ATH1LgcI4cgV+SU3VQ6bsm/gfAOQyjdHhuiaNhbXTNB9CjZmVlzQPoomZ2HaNnZW6qc2FuZG5ldC12MaJnaMQgaJXPYTdWaeTNSs8FMMzPNfV7SrHXqJgFsJLxRbSPjzCibHbNBAWjcmN2xCBWkH3PValty0Rb0cyZo69Alhp4IbNKFnhXtgJ++A9EzKNzbmTEIOJPEbccL6IqmeBeaLzbLav25U9jBMjloaIyF1eY9HFxpHR5cGWjcGF5"


class DijkstraChoice(BaseModel):
    PowerImportedKw: float
    NextNodeCostDollars: float


class CostAndQuantityBought(BaseModel):
    QuantityBought: float
    Cost: float


class SlotStuff(BaseModel):
    Slot: MarketSlot
    BidParams: Optional[FloParams] = None
    Flo: Optional[Flo] = None
    Bid: Optional[AtnBid] = None
    Price: Optional[float] = None


def dummy_bid() -> AtnBid:
    return AtnBid(
        BidderAlias="d1.isone.dummy.ta",
        BidderGNodeInstanceId="00000000-0000-0000-0000-000000000000",
        MarketSlotName="rt60gate30b.d1.isone.ver.keene.1577836800",
        BidList=[],
        SignedMarketFeeTxn=DUMMY_ALGO_TXN,
    )


def dummy_slot_stuff(slot: MarketSlot) -> SlotStuff:
    return SlotStuff(
        Slot=slot, FloStartIdx=50, BidParams=dummy_flo_params(), AtnBid=dummy_bid()
    )


def is_dummy_slot_stuff(bid_stuff: SlotStuff) -> bool:
    if is_dummy_flo_params(bid_stuff.BidParams):
        return True
    return False


def name_from_market_slot(slot: MarketSlot) -> str:
    return f"{slot.Type.Name.value}.{slot.MarketMakerAlias}.{slot.StartUnixS}"


def market_slot_from_name(market_slot_name: str) -> MarketSlot:
    """rt60gate30b.d1.isone.ver.keene.1577836800"""
    try:
        property_format.check_is_market_slot_name_lrd_format(market_slot_name)
    except ValueError as e:
        raise Exception(
            f"market slot alias {market_slot_name} does not have market"
            " slot alias lrd format!"
        )
    words = market_slot_name.split(".")
    market_type_name = words[0]
    market_type_dc = MarketType.by_id[market_type_name]
    market_type = MarketTypeGt_Maker.dc_to_tuple(market_type_dc)
    market_maker_alias = ".".join(words[1:-1])
    slot_start = int(words[-1])
    return MarketSlot(
        Type=market_type, MarketMakerAlias=market_maker_alias, StartUnixS=slot_start
    )


def is_dummy_atn_params(atn_params: AtnParams) -> bool:
    if atn_params.GNodeAlias == "d1.isone.dummy.ta":
        return True
    return False


def is_dummy_flo_params(flo_params: FloParams) -> bool:
    if flo_params.RtElecPriceUid == "00000000-0000-0000-0000-000000000000":
        return True
    return False


def dummy_flo_params() -> FloParams:
    return FloParams(
        RtElecPriceUid="00000000-0000-0000-0000-000000000000",
        WeatherUid="00000000-0000-0000-0000-000000000000",
    )

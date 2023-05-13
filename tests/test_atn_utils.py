import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.atn_utils import *


def test_market_slot_utils() -> None:
    market_slot_name = "rt60gate30b.d1.isone.ver.keene.1577836800"
    market_name = "rt60gate30b.d1.isone.ver.keene"
    slot_start_s = 1577836800
    assert market_name_from_market_slot_name(market_slot_name) == market_name
    assert slot_start_s_from_market_slot_name(market_slot_name) == slot_start_s

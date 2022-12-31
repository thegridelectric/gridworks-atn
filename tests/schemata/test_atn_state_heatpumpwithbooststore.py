"""Tests atn.state.heatpumpwithbooststore type, version 000"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.schemata import AtnStateHeatpumpwithbooststore_Maker as Maker


def test_atn_state_heatpumpwithbooststore_generated() -> None:
    d = {
        "FromGNodeAlias": "d1.isone.ver.keene.holly",
        "FromGNodeInstanceId": "d4057686-c199-4274-b595-f7e39ce863e2",
        "BoostPowerKwTimes1000": 933,
        "HeatpumpPowerKwTimes1000": 0,
        "StoreKwh": 50,
        "CopTimes10": 23,
        "MaxStoreKwh": 80,
        "AboutTerminalAssetAlias": "d1.isone.ver.keene.holly.ta",
        "TypeName": "atn.state.heatpumpwithbooststore",
        "Version": "000",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # test Maker init
    t = Maker(
        from_g_node_alias=gtuple.FromGNodeAlias,
        from_g_node_instance_id=gtuple.FromGNodeInstanceId,
        boost_power_kw_times1000=gtuple.BoostPowerKwTimes1000,
        heatpump_power_kw_times1000=gtuple.HeatpumpPowerKwTimes1000,
        store_kwh=gtuple.StoreKwh,
        cop_times10=gtuple.CopTimes10,
        max_store_kwh=gtuple.MaxStoreKwh,
        about_terminal_asset_alias=gtuple.AboutTerminalAssetAlias,
    ).tuple
    assert t == gtuple

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FromGNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FromGNodeInstanceId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["BoostPowerKwTimes1000"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HeatpumpPowerKwTimes1000"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StoreKwh"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["CopTimes10"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MaxStoreKwh"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AboutTerminalAssetAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, BoostPowerKwTimes1000="933.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, HeatpumpPowerKwTimes1000="0.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StoreKwh="50.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CopTimes10="23.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, MaxStoreKwh="80.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, FromGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeInstanceId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AboutTerminalAssetAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test

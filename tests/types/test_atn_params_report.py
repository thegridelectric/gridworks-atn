"""Tests atn.params.report type, version 000"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.types import AtnParamsReport_Maker as Maker


def test_atn_params_report_generated() -> None:
    d = {
        "GNodeAlias": "d1.isone.ver.keene.holly",
        "GNodeInstanceId": "97eba574-bd20-45b5-bf82-9ba2f492d8f6",
        "AtnParamsTypeName": "atn.params.brickstorageheater",
        "TimeUnixS": 1577836800,
        "IrlTimeUnixS": 1668127823,
        "Params": {
            "GNodeAlias": "d1.isone.ver.keene.holly",
            "HomeCity": "MILLINOCKET_ME",
            "TimezoneString": "US/Eastern",
            "CurrencyUnitGtEnumSymbol": "e57c5143",
            "TariffGtEnumSymbol": "2127aba6",
            "EnergyTypeGtEnumSymbol": "e9dc99a6",
            "StandardOfferPriceDollarsPerMwh": 110,
            "DistributionTariffDollarsPerMwh": 113,
            "MaxBrickTempC": 190,
            "RatedMaxPowerKw": 13.5,
            "C": 200,
            "ROff": 0.09,
            "ROn": 0.15,
            "RoomTempF": 70,
            "Alpha": 158,
            "BetaOt": 158,
            "TempUnitGtEnumSymbol": "6f16ee63",
            "TypeName": "atn.params.brickstorageheater",
            "Version": "000",
        },
        "TypeName": "atn.params.report",
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
        g_node_alias=gtuple.GNodeAlias,
        g_node_instance_id=gtuple.GNodeInstanceId,
        atn_params_type_name=gtuple.AtnParamsTypeName,
        time_unix_s=gtuple.TimeUnixS,
        irl_time_unix_s=gtuple.IrlTimeUnixS,
        params=gtuple.Params,
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
    del d2["GNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["GNodeInstanceId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AtnParamsTypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TimeUnixS"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Params"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "IrlTimeUnixS" in d2.keys():
        del d2["IrlTimeUnixS"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TimeUnixS="1577836800.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, IrlTimeUnixS="1668127823.1")
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

    d2 = dict(d, GNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, GNodeInstanceId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AtnParamsTypeName="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TimeUnixS=32503683600)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, IrlTimeUnixS=32503683600)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test

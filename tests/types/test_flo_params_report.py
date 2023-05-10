"""Tests flo.params.report type, version 000"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.types import FloParamsReport_Maker as Maker


def test_flo_params_report_generated() -> None:
    d = {
        "GNodeAlias": "d1.isone.ver.keene.holly",
        "GNodeInstanceId": "97eba574-bd20-45b5-bf82-9ba2f492d8f6",
        "FloParamsTypeName": "flo.params.brickstorageheater",
        "FloParamsTypeVersion": "000",
        "ReportGeneratedTimeUnixS": 1577836800,
        "IrlTimeUnixS": 1668127823,
        "Params": {
            "MaxBrickTempC": 190,
            "RatedMaxPowerKw": 13.5,
            "ROff": 0.08,
            "ROn": 0.15,
            "RoomTempF": 70,
            "CurrencyUnitGtEnumSymbol": "e57c5143",
            "TempUnitGtEnumSymbol": "6f16ee63",
            "TimezoneString": "US/Eastern",
            "HomeCity": "MILLINOCKET_ME",
            "IsRegulating": False,
            "StorageSteps": 100,
            "SliceDurationMinutes": [60],
            "PowerRequiredByHouseFromSystemAvgKwList": [3.42],
            "C": 200,
            "RealtimeElectricityPrice": [10.35],
            "OutsideTempF": [-5.1],
            "DistributionPrice": [40.0],
            "RtElecPriceUid": "bd2ec5c5-40b9-4b61-ad1b-4613370246d6",
            "RegulationPrice": [25.3],
            "WeatherUid": "3bbcb552-52e3-4b86-84e0-084959f9fc0f",
            "DistPriceUid": "b91ef8e7-50d7-4587-bf13-a3af7ecdb83a",
            "RegPriceUid": "0499a20e-7b81-47af-a2b4-8f4df0cd1284",
            "StartYearUtc": 2020,
            "StartMonthUtc": 1,
            "StartDayUtc": 1,
            "StartHourUtc": 0,
            "StartMinuteUtc": 0,
            "StartingStoreIdx": 50,
            "AmbientPowerInKw": 1.25,
            "HouseWorstCaseTempF": -7,
            "GNodeAlias": "d1.isone.ver.keene.holly",
            "FloParamsUid": "97eba574-bd20-45b5-bf82-9ba2f492d8f6",
            "TypeName": "flo.params.brickstorageheater",
            "Version": "000",
        },
        "TypeName": "flo.params.report",
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
        flo_params_type_name=gtuple.FloParamsTypeName,
        flo_params_type_version=gtuple.FloParamsTypeVersion,
        report_generated_time_unix_s=gtuple.ReportGeneratedTimeUnixS,
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
    del d2["FloParamsTypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FloParamsTypeVersion"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ReportGeneratedTimeUnixS"]
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

    d2 = dict(d, ReportGeneratedTimeUnixS="1577836800.1")
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

    d2 = dict(d, FloParamsTypeName="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReportGeneratedTimeUnixS=32503683600)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, IrlTimeUnixS=32503683600)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test

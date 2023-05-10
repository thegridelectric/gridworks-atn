"""Tests flo.params.brickstorageheater type, version 000"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.enums import RecognizedCurrencyUnit
from gwatn.enums import RecognizedTemperatureUnit
from gwatn.types import FloParamsBrickstorageheater_Maker as Maker


def test_flo_params_brickstorageheater_generated() -> None:
    d = {
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
        "GNodeAlias": "d1.isone.ver.keene.holly",
        "FloParamsUid": "97eba574-bd20-45b5-bf82-9ba2f492d8f6",
        "TypeName": "flo.params.brickstorageheater",
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
        max_brick_temp_c=gtuple.MaxBrickTempC,
        rated_max_power_kw=gtuple.RatedMaxPowerKw,
        r_off=gtuple.ROff,
        r_on=gtuple.ROn,
        room_temp_f=gtuple.RoomTempF,
        currency_unit=gtuple.CurrencyUnit,
        temp_unit=gtuple.TempUnit,
        timezone_string=gtuple.TimezoneString,
        home_city=gtuple.HomeCity,
        is_regulating=gtuple.IsRegulating,
        storage_steps=gtuple.StorageSteps,
        slice_duration_minutes=gtuple.SliceDurationMinutes,
        power_required_by_house_from_system_avg_kw_list=gtuple.PowerRequiredByHouseFromSystemAvgKwList,
        realtime_electricity_price=gtuple.RealtimeElectricityPrice,
        outside_temp_f=gtuple.OutsideTempF,
        distribution_price=gtuple.DistributionPrice,
        rt_elec_price_uid=gtuple.RtElecPriceUid,
        regulation_price=gtuple.RegulationPrice,
        weather_uid=gtuple.WeatherUid,
        dist_price_uid=gtuple.DistPriceUid,
        reg_price_uid=gtuple.RegPriceUid,
        start_year_utc=gtuple.StartYearUtc,
        start_month_utc=gtuple.StartMonthUtc,
        start_day_utc=gtuple.StartDayUtc,
        start_hour_utc=gtuple.StartHourUtc,
        start_minute_utc=gtuple.StartMinuteUtc,
        starting_store_idx=gtuple.StartingStoreIdx,
        g_node_alias=gtuple.GNodeAlias,
        flo_params_uid=gtuple.FloParamsUid,
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
    del d2["MaxBrickTempC"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RatedMaxPowerKw"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ROff"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ROn"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RoomTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["CurrencyUnitGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TempUnitGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TimezoneString"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HomeCity"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["IsRegulating"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StorageSteps"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SliceDurationMinutes"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["PowerRequiredByHouseFromSystemAvgKwList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RealtimeElectricityPrice"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["OutsideTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["DistributionPrice"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RtElecPriceUid"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RegulationPrice"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["WeatherUid"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StartYearUtc"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StartMonthUtc"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StartDayUtc"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StartHourUtc"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StartMinuteUtc"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StartingStoreIdx"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["GNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FloParamsUid"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "DistPriceUid" in d2.keys():
        del d2["DistPriceUid"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "RegPriceUid" in d2.keys():
        del d2["RegPriceUid"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, MaxBrickTempC="190.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RatedMaxPowerKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ROff="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ROn="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RoomTempF="70.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CurrencyUnitGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).CurrencyUnit = RecognizedCurrencyUnit.default()

    d2 = dict(d, TempUnitGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).TempUnit = RecognizedTemperatureUnit.default()

    d2 = dict(d, IsRegulating="this is not a boolean")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StorageSteps="100.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StartYearUtc="2020.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StartMonthUtc="1.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StartDayUtc="1.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StartHourUtc="0.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StartMinuteUtc="0.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StartingStoreIdx="50.1")
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

    d2 = dict(d, RtElecPriceUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, WeatherUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, DistPriceUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RegPriceUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, GNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FloParamsUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test

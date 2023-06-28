"""Tests flo.params.simpleresistivehydronic type, version 000"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.enums import DistributionTariff
from gwatn.enums import EnergySupplyType
from gwatn.enums import RecognizedCurrencyUnit
from gwatn.types import FloParamsSimpleresistivehydronic_Maker as Maker


def test_flo_params_simpleresistivehydronic_generated() -> None:
    d = {
        "GNodeAlias": "d1.isone.ver.keene.holly",
        "FloParamsUid": "97eba574-bd20-45b5-bf82-9ba2f492d8f6",
        "HomeCity": "MILLINOCKET_ME",
        "TimezoneString": "US/Eastern",
        "StartYearUtc": 2020,
        "StartMonthUtc": 1,
        "StartDayUtc": 1,
        "StartHourUtc": 0,
        "StartMinuteUtc": 0,
        "StorageSteps": 100,
        "StoreSizeGallons": 240,
        "MaxStoreTempF": 210,
        "RatedPowerKw": 9.5,
        "RequiredSourceWaterTempF": 120,
        "CirculatorPumpGpm": 4.5,
        "ReturnWaterDeltaTempF": 20,
        "RoomTempF": 70,
        "AmbientPowerInKw": 1.2,
        "HouseWorstCaseTempF": -7,
        "StorePassiveLossRatio": 0.005,
        "PowerLostFromHouseKwList": [3.42],
        "AmbientTempStoreF": 65,
        "SliceDurationMinutes": [60],
        "RealtimeElectricityPrice": [10.35],
        "DistributionPrice": [40.0],
        "OutsideTempF": [-5.1],
        "RtElecPriceUid": "bd2ec5c5-40b9-4b61-ad1b-4613370246d6",
        "DistPriceUid": "b91ef8e7-50d7-4587-bf13-a3af7ecdb83a",
        "WeatherUid": "3bbcb552-52e3-4b86-84e0-084959f9fc0f",
        "CurrencyUnitGtEnumSymbol": "e57c5143",
        "TariffGtEnumSymbol": "2127aba6",
        "EnergyTypeGtEnumSymbol": "e9dc99a6",
        "StandardOfferPriceDollarsPerMwh": 110,
        "FlatDistributionTariffDollarsPerMwh": 113,
        "StartingStoreIdx": 50,
        "TypeName": "flo.params.simpleresistivehydronic",
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
        flo_params_uid=gtuple.FloParamsUid,
        home_city=gtuple.HomeCity,
        timezone_string=gtuple.TimezoneString,
        start_year_utc=gtuple.StartYearUtc,
        start_month_utc=gtuple.StartMonthUtc,
        start_day_utc=gtuple.StartDayUtc,
        start_hour_utc=gtuple.StartHourUtc,
        start_minute_utc=gtuple.StartMinuteUtc,
        storage_steps=gtuple.StorageSteps,
        store_size_gallons=gtuple.StoreSizeGallons,
        max_store_temp_f=gtuple.MaxStoreTempF,
        rated_power_kw=gtuple.RatedPowerKw,
        required_source_water_temp_f=gtuple.RequiredSourceWaterTempF,
        circulator_pump_gpm=gtuple.CirculatorPumpGpm,
        return_water_delta_temp_f=gtuple.ReturnWaterDeltaTempF,
        room_temp_f=gtuple.RoomTempF,
        ambient_power_in_kw=gtuple.AmbientPowerInKw,
        house_worst_case_temp_f=gtuple.HouseWorstCaseTempF,
        store_passive_loss_ratio=gtuple.StorePassiveLossRatio,
        power_lost_from_house_kw_list=gtuple.PowerLostFromHouseKwList,
        ambient_temp_store_f=gtuple.AmbientTempStoreF,
        slice_duration_minutes=gtuple.SliceDurationMinutes,
        realtime_electricity_price=gtuple.RealtimeElectricityPrice,
        distribution_price=gtuple.DistributionPrice,
        outside_temp_f=gtuple.OutsideTempF,
        rt_elec_price_uid=gtuple.RtElecPriceUid,
        dist_price_uid=gtuple.DistPriceUid,
        weather_uid=gtuple.WeatherUid,
        currency_unit=gtuple.CurrencyUnit,
        tariff=gtuple.Tariff,
        energy_type=gtuple.EnergyType,
        standard_offer_price_dollars_per_mwh=gtuple.StandardOfferPriceDollarsPerMwh,
        flat_distribution_tariff_dollars_per_mwh=gtuple.FlatDistributionTariffDollarsPerMwh,
        starting_store_idx=gtuple.StartingStoreIdx,
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
    del d2["FloParamsUid"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HomeCity"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TimezoneString"]
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
    del d2["StorageSteps"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StoreSizeGallons"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MaxStoreTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RatedPowerKw"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RequiredSourceWaterTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["CirculatorPumpGpm"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ReturnWaterDeltaTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RoomTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AmbientPowerInKw"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HouseWorstCaseTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StorePassiveLossRatio"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["PowerLostFromHouseKwList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AmbientTempStoreF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SliceDurationMinutes"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RealtimeElectricityPrice"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["DistributionPrice"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["OutsideTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RtElecPriceUid"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["DistPriceUid"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["WeatherUid"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["CurrencyUnitGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TariffGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["EnergyTypeGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StandardOfferPriceDollarsPerMwh"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FlatDistributionTariffDollarsPerMwh"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StartingStoreIdx"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

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

    d2 = dict(d, StorageSteps="100.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StoreSizeGallons="240.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, MaxStoreTempF="210.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RatedPowerKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RequiredSourceWaterTempF="120.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CirculatorPumpGpm="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReturnWaterDeltaTempF="20.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RoomTempF="70.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AmbientPowerInKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, HouseWorstCaseTempF="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StorePassiveLossRatio="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AmbientTempStoreF="65.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CurrencyUnitGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).CurrencyUnit = RecognizedCurrencyUnit.default()

    d2 = dict(d, TariffGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).Tariff = DistributionTariff.default()

    d2 = dict(d, EnergyTypeGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).EnergyType = EnergySupplyType.default()

    d2 = dict(d, StandardOfferPriceDollarsPerMwh="110.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FlatDistributionTariffDollarsPerMwh="113.1")
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

    d2 = dict(d, GNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FloParamsUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RtElecPriceUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, DistPriceUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, WeatherUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test

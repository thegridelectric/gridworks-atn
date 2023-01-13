"""Tests flo.params.heatpumpwithbooststore type, version 000"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.enums import DistributionTariff
from gwatn.enums import EmitterPumpFeedbackModel
from gwatn.enums import EnergySupplyType
from gwatn.enums import MixingValveFeedbackModel
from gwatn.enums import RecognizedCurrencyUnit
from gwatn.enums import RecognizedTemperatureUnit
from gwatn.types import FloParamsHeatpumpwithbooststore_Maker as Maker


def test_flo_params_heatpumpwithbooststore_generated() -> None:
    d = {
        "StoreSizeGallons": 240,
        "MaxStoreTempF": 190,
        "StoreMaxPowerKw": 9,
        "RatedHeatpumpElectricityKw": 5.5,
        "MaxHeatpumpSourceWaterTempF": 135,
        "SystemMaxHeatOutputSwtF": 160,
        "SystemMaxHeatOutputDeltaTempF": 20,
        "SystemMaxHeatOutputGpm": 6,
        "EmitterMaxSafeSwtF": 170,
        "CirculatorPumpMaxGpm": 10,
        "HeatpumpTariffGtEnumSymbol": "2127aba6",
        "HeatpumpEnergySupplyTypeGtEnumSymbol": "e9dc99a6",
        "BoostTariffGtEnumSymbol": "2127aba6",
        "BoostEnergySupplyTypeGtEnumSymbol": "e9dc99a6",
        "StandardOfferPriceDollarsPerMwh": 110,
        "DistributionTariffDollarsPerMwh": 113,
        "AmbientTempStoreF": 65,
        "StorePassiveLossRatio": 0.001,
        "RoomTempF": 70,
        "AmbientPowerInKw": 1.25,
        "ZeroPotentialEnergyWaterTempF": 100,
        "EmitterPumpFeedbackModelGtEnumSymbol": "00000000",
        "MixingValveFeedbackModelGtEnumSymbol": "0397c1df",
        "CautiousMixingValveTempDeltaF": 5,
        "Cop1TempF": -20,
        "Cop4TempF": 70,
        "CurrencyUnitGtEnumSymbol": "e57c5143",
        "TempUnitGtEnumSymbol": "6f16ee63",
        "TimezoneString": "US/Eastern",
        "HomeCity": "MILLINOCKET_ME",
        "StorageSteps": 100,
        "HouseWorstCaseTempF": -7,
        "SystemMaxHeatOutputKwAvg": 11.68,
        "K": -1.1,
        "IsRegulating": False,
        "SliceDurationMinutes": [60],
        "PowerRequiredByHouseFromSystemAvgKwList": [3.42],
        "OutsideTempF": [-5.1],
        "RealtimeElectricityPrice": [10.35],
        "DistributionPrice": [40.0],
        "RegulationPrice": [25.3],
        "RtElecPriceUid": "bd2ec5c5-40b9-4b61-ad1b-4613370246d6",
        "WeatherUid": "3bbcb552-52e3-4b86-84e0-084959f9fc0f",
        "DistPriceUid": "b91ef8e7-50d7-4587-bf13-a3af7ecdb83a",
        "RegPriceUid": "0499a20e-7b81-47af-a2b4-8f4df0cd1284",
        "StartYearUtc": 2020,
        "StartMonthUtc": 1,
        "StartDayUtc": 1,
        "StartHourUtc": 0,
        "StartMinuteUtc": 0,
        "StartingStoreIdx": 50,
        "TypeName": "flo.params.heatpumpwithbooststore",
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
        store_size_gallons=gtuple.StoreSizeGallons,
        max_store_temp_f=gtuple.MaxStoreTempF,
        store_max_power_kw=gtuple.StoreMaxPowerKw,
        rated_heatpump_electricity_kw=gtuple.RatedHeatpumpElectricityKw,
        max_heatpump_source_water_temp_f=gtuple.MaxHeatpumpSourceWaterTempF,
        system_max_heat_output_swt_f=gtuple.SystemMaxHeatOutputSwtF,
        system_max_heat_output_delta_temp_f=gtuple.SystemMaxHeatOutputDeltaTempF,
        system_max_heat_output_gpm=gtuple.SystemMaxHeatOutputGpm,
        emitter_max_safe_swt_f=gtuple.EmitterMaxSafeSwtF,
        circulator_pump_max_gpm=gtuple.CirculatorPumpMaxGpm,
        heatpump_tariff=gtuple.HeatpumpTariff,
        heatpump_energy_supply_type=gtuple.HeatpumpEnergySupplyType,
        boost_tariff=gtuple.BoostTariff,
        boost_energy_supply_type=gtuple.BoostEnergySupplyType,
        standard_offer_price_dollars_per_mwh=gtuple.StandardOfferPriceDollarsPerMwh,
        distribution_tariff_dollars_per_mwh=gtuple.DistributionTariffDollarsPerMwh,
        ambient_temp_store_f=gtuple.AmbientTempStoreF,
        store_passive_loss_ratio=gtuple.StorePassiveLossRatio,
        room_temp_f=gtuple.RoomTempF,
        ambient_power_in_kw=gtuple.AmbientPowerInKw,
        zero_potential_energy_water_temp_f=gtuple.ZeroPotentialEnergyWaterTempF,
        emitter_pump_feedback_model=gtuple.EmitterPumpFeedbackModel,
        mixing_valve_feedback_model=gtuple.MixingValveFeedbackModel,
        cautious_mixing_valve_temp_delta_f=gtuple.CautiousMixingValveTempDeltaF,
        cop1_temp_f=gtuple.Cop1TempF,
        cop4_temp_f=gtuple.Cop4TempF,
        currency_unit=gtuple.CurrencyUnit,
        temp_unit=gtuple.TempUnit,
        timezone_string=gtuple.TimezoneString,
        home_city=gtuple.HomeCity,
        storage_steps=gtuple.StorageSteps,
        house_worst_case_temp_f=gtuple.HouseWorstCaseTempF,
        system_max_heat_output_kw_avg=gtuple.SystemMaxHeatOutputKwAvg,
        k=gtuple.K,
        is_regulating=gtuple.IsRegulating,
        slice_duration_minutes=gtuple.SliceDurationMinutes,
        power_required_by_house_from_system_avg_kw_list=gtuple.PowerRequiredByHouseFromSystemAvgKwList,
        outside_temp_f=gtuple.OutsideTempF,
        realtime_electricity_price=gtuple.RealtimeElectricityPrice,
        distribution_price=gtuple.DistributionPrice,
        regulation_price=gtuple.RegulationPrice,
        rt_elec_price_uid=gtuple.RtElecPriceUid,
        weather_uid=gtuple.WeatherUid,
        dist_price_uid=gtuple.DistPriceUid,
        reg_price_uid=gtuple.RegPriceUid,
        start_year_utc=gtuple.StartYearUtc,
        start_month_utc=gtuple.StartMonthUtc,
        start_day_utc=gtuple.StartDayUtc,
        start_hour_utc=gtuple.StartHourUtc,
        start_minute_utc=gtuple.StartMinuteUtc,
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
    del d2["StoreSizeGallons"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MaxStoreTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StoreMaxPowerKw"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RatedHeatpumpElectricityKw"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MaxHeatpumpSourceWaterTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SystemMaxHeatOutputSwtF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SystemMaxHeatOutputDeltaTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SystemMaxHeatOutputGpm"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["EmitterMaxSafeSwtF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["CirculatorPumpMaxGpm"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HeatpumpTariffGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HeatpumpEnergySupplyTypeGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["BoostTariffGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["BoostEnergySupplyTypeGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StandardOfferPriceDollarsPerMwh"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["DistributionTariffDollarsPerMwh"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AmbientTempStoreF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StorePassiveLossRatio"]
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
    del d2["ZeroPotentialEnergyWaterTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["EmitterPumpFeedbackModelGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MixingValveFeedbackModelGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["CautiousMixingValveTempDeltaF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Cop1TempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Cop4TempF"]
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
    del d2["StorageSteps"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HouseWorstCaseTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SystemMaxHeatOutputKwAvg"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["K"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["IsRegulating"]
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
    del d2["OutsideTempF"]
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
    del d2["RegulationPrice"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RtElecPriceUid"]
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

    d2 = dict(d, StoreSizeGallons="240.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, MaxStoreTempF="190.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StoreMaxPowerKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RatedHeatpumpElectricityKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, MaxHeatpumpSourceWaterTempF="135.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SystemMaxHeatOutputSwtF="160.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SystemMaxHeatOutputDeltaTempF="20.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SystemMaxHeatOutputGpm="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EmitterMaxSafeSwtF="170.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CirculatorPumpMaxGpm="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, HeatpumpTariffGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).HeatpumpTariff = DistributionTariff.default()

    d2 = dict(d, HeatpumpEnergySupplyTypeGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).HeatpumpEnergySupplyType = EnergySupplyType.default()

    d2 = dict(d, BoostTariffGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).BoostTariff = DistributionTariff.default()

    d2 = dict(d, BoostEnergySupplyTypeGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).BoostEnergySupplyType = EnergySupplyType.default()

    d2 = dict(d, StandardOfferPriceDollarsPerMwh="110.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, DistributionTariffDollarsPerMwh="113.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AmbientTempStoreF="65.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StorePassiveLossRatio="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RoomTempF="70.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AmbientPowerInKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ZeroPotentialEnergyWaterTempF="100.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EmitterPumpFeedbackModelGtEnumSymbol="hi")
    Maker.dict_to_tuple(
        d2
    ).EmitterPumpFeedbackModel = EmitterPumpFeedbackModel.default()

    d2 = dict(d, MixingValveFeedbackModelGtEnumSymbol="hi")
    Maker.dict_to_tuple(
        d2
    ).MixingValveFeedbackModel = MixingValveFeedbackModel.default()

    d2 = dict(d, CautiousMixingValveTempDeltaF="5.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Cop1TempF="-20.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Cop4TempF="70.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CurrencyUnitGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).CurrencyUnit = RecognizedCurrencyUnit.default()

    d2 = dict(d, TempUnitGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).TempUnit = RecognizedTemperatureUnit.default()

    d2 = dict(d, StorageSteps="100.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, HouseWorstCaseTempF="-7.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SystemMaxHeatOutputKwAvg="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, K="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, IsRegulating="this is not a boolean")
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

    # End of Test

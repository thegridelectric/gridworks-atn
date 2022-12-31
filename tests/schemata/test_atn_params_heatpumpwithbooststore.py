"""Tests atn.params.heatpumpwithbooststore type, version 000"""
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
from gwatn.schemata import AtnParamsHeatpumpwithbooststore_Maker as Maker


def test_atn_params_heatpumpwithbooststore_generated() -> None:
    d = {
        "StoreSizeGallons": 240,
        "MaxStoreTempF": 190,
        "StoreMaxPowerKw": 13.5,
        "RatedHeatpumpElectricityKw": 5.5,
        "MaxHeatpumpSourceWaterTempF": 135,
        "SystemMaxHeatOutputSwtF": 160,
        "SystemMaxHeatOutputDeltaTempF": 20,
        "SystemMaxHeatOutputGpm": 4,
        "EmitterMaxSafeSwtF": 170,
        "CirculatorPumpMaxGpm": 12,
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
        "FloSlices": 48,
        "SliceDurationMinutes": 60,
        "HouseWorstCaseTempF": -7,
        "AnnualHvacKwhTh": 28125,
        "BetaOt": 158,
        "HouseHeatingCapacity": 4,
        "GNodeAlias": "d1.isone.ver.keene.holly",
        "GNodeInstanceId": "c8bb41eb-dad3-4e1d-8069-482f1a464225",
        "TypeName": "atn.params.heatpumpwithbooststore",
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
        flo_slices=gtuple.FloSlices,
        slice_duration_minutes=gtuple.SliceDurationMinutes,
        house_worst_case_temp_f=gtuple.HouseWorstCaseTempF,
        annual_hvac_kwh_th=gtuple.AnnualHvacKwhTh,
        beta_ot=gtuple.BetaOt,
        house_heating_capacity=gtuple.HouseHeatingCapacity,
        g_node_alias=gtuple.GNodeAlias,
        g_node_instance_id=gtuple.GNodeInstanceId,
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
    del d2["FloSlices"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SliceDurationMinutes"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HouseWorstCaseTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AnnualHvacKwhTh"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["BetaOt"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["HouseHeatingCapacity"]
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

    d2 = dict(d, FloSlices="48.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SliceDurationMinutes="60.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, HouseWorstCaseTempF="-7.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AnnualHvacKwhTh="28125.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, BetaOt="158.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, HouseHeatingCapacity="this is not a float")
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

    # End of Test

"""Tests atn.params.simpleresistivehydronic type, version 000"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.enums import DistributionTariff
from gwatn.enums import EnergySupplyType
from gwatn.enums import RecognizedCurrencyUnit
from gwatn.types import AtnParamsSimpleresistivehydronic_Maker as Maker


def test_atn_params_simpleresistivehydronic_generated() -> None:
    d = {
        "GNodeAlias": "d1.isone.ver.keene.holly",
        "HomeCity": "MILLINOCKET_ME",
        "TimezoneString": "US/Eastern",
        "StorageSteps": 100,
        "FloSlices": 48,
        "SliceDurationMinutes": 60,
        "CurrencyUnitGtEnumSymbol": "e57c5143",
        "TariffGtEnumSymbol": "2127aba6",
        "EnergyTypeGtEnumSymbol": "e9dc99a6",
        "StandardOfferPriceDollarsPerMwh": 110,
        "DistributionTariffDollarsPerMwh": 113,
        "StoreSizeGallons": 240,
        "MaxStoreTempF": 210,
        "ElementMaxPowerKw": 9.5,
        "RequiredSourceWaterTempF": 120,
        "FixedPumpGpm": 5.5,
        "ReturnWaterFixedDeltaT": 20,
        "AnnualHvacKwhTh": 25000,
        "AmbientPowerInKw": 1.2,
        "HouseWorstCaseTempF": -7,
        "RoomTempF": 68,
        "TypeName": "atn.params.simpleresistivehydronic",
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
        home_city=gtuple.HomeCity,
        timezone_string=gtuple.TimezoneString,
        storage_steps=gtuple.StorageSteps,
        flo_slices=gtuple.FloSlices,
        slice_duration_minutes=gtuple.SliceDurationMinutes,
        currency_unit=gtuple.CurrencyUnit,
        tariff=gtuple.Tariff,
        energy_type=gtuple.EnergyType,
        standard_offer_price_dollars_per_mwh=gtuple.StandardOfferPriceDollarsPerMwh,
        distribution_tariff_dollars_per_mwh=gtuple.DistributionTariffDollarsPerMwh,
        store_size_gallons=gtuple.StoreSizeGallons,
        max_store_temp_f=gtuple.MaxStoreTempF,
        element_max_power_kw=gtuple.ElementMaxPowerKw,
        required_source_water_temp_f=gtuple.RequiredSourceWaterTempF,
        fixed_pump_gpm=gtuple.FixedPumpGpm,
        return_water_fixed_delta_t=gtuple.ReturnWaterFixedDeltaT,
        annual_hvac_kwh_th=gtuple.AnnualHvacKwhTh,
        ambient_power_in_kw=gtuple.AmbientPowerInKw,
        house_worst_case_temp_f=gtuple.HouseWorstCaseTempF,
        room_temp_f=gtuple.RoomTempF,
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
    del d2["HomeCity"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TimezoneString"]
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
    del d2["DistributionTariffDollarsPerMwh"]
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
    del d2["ElementMaxPowerKw"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RequiredSourceWaterTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FixedPumpGpm"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ReturnWaterFixedDeltaT"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AnnualHvacKwhTh"]
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
    del d2["RoomTempF"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, StorageSteps="100.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FloSlices="48.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SliceDurationMinutes="60.1")
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

    d2 = dict(d, DistributionTariffDollarsPerMwh="113.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StoreSizeGallons="240.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, MaxStoreTempF="210.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ElementMaxPowerKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RequiredSourceWaterTempF="120.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FixedPumpGpm="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReturnWaterFixedDeltaT="20.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AnnualHvacKwhTh="25000.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AmbientPowerInKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, HouseWorstCaseTempF="-7.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RoomTempF="68.1")
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

    # End of Test

"""Tests atn.params.brickstorageheater type, version 000"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.enums import DistributionTariff
from gwatn.enums import EnergySupplyType
from gwatn.enums import RecognizedCurrencyUnit
from gwatn.enums import RecognizedTemperatureUnit
from gwatn.types import AtnParamsBrickstorageheater_Maker as Maker


def test_atn_params_brickstorageheater_generated() -> None:
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
        "MaxBrickTempC": 190,
        "RatedMaxPowerKw": 13.5,
        "C": 200,
        "ROff": 0.08,
        "ROn": 0.15,
        "RoomTempF": 70,
        "AnnualHvacKwhTh": 28125,
        "BetaOt": 158,
        "TempUnitGtEnumSymbol": "6f16ee63",
        "AmbientPowerInKw": 1.25,
        "HouseWorstCaseTempF": -7,
        "TypeName": "atn.params.brickstorageheater",
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
        max_brick_temp_c=gtuple.MaxBrickTempC,
        rated_max_power_kw=gtuple.RatedMaxPowerKw,
        c=gtuple.C,
        r_off=gtuple.ROff,
        r_on=gtuple.ROn,
        room_temp_f=gtuple.RoomTempF,
        annual_hvac_kwh_th=gtuple.AnnualHvacKwhTh,
        beta_ot=gtuple.BetaOt,
        temp_unit=gtuple.TempUnit,
        ambient_power_in_kw=gtuple.AmbientPowerInKw,
        house_worst_case_temp_f=gtuple.HouseWorstCaseTempF,
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
    del d2["MaxBrickTempC"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RatedMaxPowerKw"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["C"]
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
    del d2["AnnualHvacKwhTh"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["BetaOt"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TempUnitGtEnumSymbol"]
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

    d2 = dict(d, MaxBrickTempC="190.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RatedMaxPowerKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, C="this is not a float")
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

    d2 = dict(d, AnnualHvacKwhTh="28125.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, BetaOt="158.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TempUnitGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).TempUnit = RecognizedTemperatureUnit.default()

    d2 = dict(d, AmbientPowerInKw="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, HouseWorstCaseTempF="-7.1")
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

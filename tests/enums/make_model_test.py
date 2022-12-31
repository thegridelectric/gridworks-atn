"""Tests for schema enum spaceheat.make.model.000"""
from gwatn.enums import MakeModel


def test_make_model() -> None:
    assert set(MakeModel.values()) == set(
        [
            "FREEDOM__RELAY",
            "OMEGAEZO__FTB800FLO",
            "UNKNOWNMAKE__UNKNOWNMODEL",
            "GRIDWORKS__SIMBOOL30AMPRELAY",
            "MAGNELAB__SCT0300050",
            "YMDC__SCT013100",
            "G1__NCD_ADS1115__TEWA_NTC_10K_A",
            "G1__NCD_ADS1115__AMPH_NTC_10K_A",
            "GRIDWORKS__SIMPM1",
            "GRIDWORKS__WATERTEMPHIGHPRECISION",
            "NCD__PR814SPST",
            "ADAFRUIT__642",
            "SCHNEIDERELECTRIC__IEM3455",
            "OPENENERGY__EMONPI",
            "EGAUGE__3010",
            "RHEEM__XE50T10H45U0",
        ]
    )

    assert MakeModel.default() == MakeModel.UNKNOWNMAKE__UNKNOWNMODEL

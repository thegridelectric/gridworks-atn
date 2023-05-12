"""Tests for schema enum recognized.irradiance.type.000"""
from gwatn.enums import RecognizedIrradianceType


def test_recognized_irradiance_type() -> None:
    assert set(RecognizedIrradianceType.values()) == {
        "PlaneOfArray",
        "Hor",
    }

    assert RecognizedIrradianceType.default() == RecognizedIrradianceType.PlaneOfArray

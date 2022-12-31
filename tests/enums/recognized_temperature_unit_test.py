"""Tests for schema enum recognized.temperature.unit.000"""
from gwatn.enums import RecognizedTemperatureUnit


def test_recognized_temperature_unit() -> None:
    assert set(RecognizedTemperatureUnit.values()) == set(
        [
            "C",
            "F",
        ]
    )

    assert RecognizedTemperatureUnit.default() == RecognizedTemperatureUnit.C

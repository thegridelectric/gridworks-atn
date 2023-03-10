"""Tests for schema enum spaceheat.unit.000"""
from gwatn.enums import Unit


def test_unit() -> None:
    assert set(Unit.values()) == {
        "Unknown",
        "Unitless",
        "W",
        "Celcius",
        "Fahrenheit",
        "Gpm",
        "WattHours",
        "AmpsRms",
        "VoltsRms",
        "Gallons",
    }

    assert Unit.default() == Unit.Unknown

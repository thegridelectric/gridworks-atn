"""Tests for schema enum spaceheat.unit.000"""
from gwatn.enums import Unit


def test_unit() -> None:
    assert set(Unit.values()) == set(
        [
            "Unknown",
            "Unitless",
            "W",
            "Celcius",
            "Fahrenheit",
            "Gpm",
            "Wh",
            "AmpsRms",
            "VoltsRms",
        ]
    )

    assert Unit.default() == Unit.Unknown

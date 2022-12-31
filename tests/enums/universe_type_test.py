"""Tests for schema enum universe.type.000"""
from gwatn.enums import UniverseType


def test_universe_type() -> None:
    assert set(UniverseType.values()) == set(
        [
            "Dev",
            "Hybrid",
        ]
    )

    assert UniverseType.default() == UniverseType.Dev

"""Tests for schema enum energy.supply.type.000"""
from gwatn.enums import EnergySupplyType


def test_energy_supply_type() -> None:
    assert set(EnergySupplyType.values()) == {
        "Unknown",
        "StandardOffer",
        "RealtimeLocalLmp",
    }

    assert EnergySupplyType.default() == EnergySupplyType.Unknown

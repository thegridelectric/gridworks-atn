"""Tests for schema enum distribution.tariff.000"""
from gwatn.enums import DistributionTariff


def test_distribution_tariff() -> None:
    assert set(DistributionTariff.values()) == {
        "Unknown",
        "VersantA1StorageHeatTariff",
        "VersantATariff",
        "VersantA20HeatTariff",
    }

    assert DistributionTariff.default() == DistributionTariff.Unknown

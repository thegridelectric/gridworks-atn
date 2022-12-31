"""Tests for schema enum atn.spaceheat.strategy.name.000"""
from gwatn.enums import AtnSpaceheatStrategyName


def test_atn_spaceheat_strategy_name() -> None:
    assert set(AtnSpaceheatStrategyName.values()) == {
        "NoActor",
        "SupervisorA",
        "HeatPumpWithBoostStore",
    }

    assert AtnSpaceheatStrategyName.default() == AtnSpaceheatStrategyName.NoActor

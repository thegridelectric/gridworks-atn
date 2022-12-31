"""Tests for schema enum strategy.name.000"""
from gwatn.enums import StrategyName


def test_strategy_name() -> None:
    assert set(StrategyName.values()) == set(
        [
            "NoActor",
            "WorldA",
            "SupervisorA",
            "AtnHeatPumpWithBoostStore",
            "TcGlobalA",
            "MarketMakerA",
        ]
    )

    assert StrategyName.default() == StrategyName.NoActor

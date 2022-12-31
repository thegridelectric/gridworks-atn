"""Tests for schema enum market.quantity.unit.000"""
from gwatn.enums import MarketQuantityUnit


def test_market_quantity_unit() -> None:
    assert set(MarketQuantityUnit.values()) == set(
        [
            "AvgMW",
            "AvgkW",
        ]
    )

    assert MarketQuantityUnit.default() == MarketQuantityUnit.AvgMW

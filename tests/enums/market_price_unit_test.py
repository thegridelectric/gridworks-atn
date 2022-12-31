"""Tests for schema enum market.price.unit.000"""
from gwatn.enums import MarketPriceUnit


def test_market_price_unit() -> None:
    assert set(MarketPriceUnit.values()) == set(
        [
            "USDPerMWh",
        ]
    )

    assert MarketPriceUnit.default() == MarketPriceUnit.USDPerMWh

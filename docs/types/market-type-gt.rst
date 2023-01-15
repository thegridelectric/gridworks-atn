MarketTypeGt
==========================
Python pydantic class corresponding to  json type ```market.type.gt```.

.. autoclass:: gwatn.types.MarketTypeGt
    :members:

**Name**:
    - Description: Name of the MarketType

**DurationMinutes**:
    - Description: Duration of MarketSlots, in minutes

**GateClosingSeconds**:
    - Description: Seconds before the start of a MarketSlot after which bids are not accepted

**PriceUnit**:
    - Description: Price Unit for market (e.g. USD Per MWh)

**QuantityUnit**:
    - Description: Quantity Unit for market (e.g. AvgMW)

**CurrencyUnit**:
    - Description: Currency Unit for market (e.g. USD)

**PriceMax**:
    - Description: PMax, required for defining bids

.. autoclass:: gwatn.types.MarketTypeGt_Maker
    :members:

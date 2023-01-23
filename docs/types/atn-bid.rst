AtnBid
==========================
Python pydantic class corresponding to  json type ```atn.bid```.

.. autoclass:: gwatn.types.AtnBid
    :members:

**BidderAlias**:
    - Description:
    - Format: LeftRightDot

**BidderGNodeInstanceId**:
    - Description:
    - Format: UuidCanonicalTextual

**MarketSlotName**:
    - Description:
    - Format: MarketSlotNameLrdFormat

**PqPairs**:
    - Description: Price Quantity Pairs. The list of Price Quantity Pairs making up the bid. The units are provided by the AtnBid.PriceUnit and AtnBid.QuantityUnit.

**InjectionIsPositive**:
    - Description:

**PriceUnit**:
    - Description:

**QuantityUnit**:
    - Description:

**SignedMarketFeeTxn**:
    - Description:
    - Format: AlgoMsgPackEncoded

.. autoclass:: gwatn.types.atn_bid.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwatn.types.atn_bid.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.atn_bid.check_is_market_slot_name_lrd_format
    :members:


.. autoclass:: gwatn.types.atn_bid.check_is_algo_address_string_format
    :members:


.. autoclass:: gwatn.types.atn_bid.check_is_algo_msg_pack_encoded
    :members:


.. autoclass:: gwatn.types.AtnBid_Maker
    :members:

HeartbeatB
==========================
Python pydantic class corresponding to  json type ```heartbeat.b```.

.. autoclass:: gwatn.types.HeartbeatB
    :members:

**FromGNodeAlias**:
    - Description: My GNodeAlias
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: My GNodeInstanceId
    - Format: UuidCanonicalTextual

**MyHex**:
    - Description: Hex character getting sent
    - Format: HexChar

**YourLastHex**:
    - Description: Last hex character received from heartbeat partner.
    - Format: HexChar

**LastReceivedTimeUnixMs**:
    - Description: Time YourLastHex was received on my clock
    - Format: ReasonableUnixTimeMs

**SendTimeUnixMs**:
    - Description: Time this message is made and sent on my clock
    - Format: ReasonableUnixTimeMs

**StartingOver**:
    - Description: True if the heartbeat initiator wants to start the volley over.  (typically the AtomicTNode in an AtomicTNode / SCADA pair) wants to start the heartbeating volley over. The result is that its partner will not expect the initiator to know its last Hex.

.. autoclass:: gwatn.types.heartbeat_b.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwatn.types.heartbeat_b.check_is_hex_char
    :members:


.. autoclass:: gwatn.types.heartbeat_b.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.heartbeat_b.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwatn.types.HeartbeatB_Maker
    :members:

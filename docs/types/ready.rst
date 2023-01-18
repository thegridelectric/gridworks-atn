Ready
==========================
Python pydantic class corresponding to  json type ```ready```.

.. autoclass:: gwatn.types.Ready
    :members:

**FromGNodeAlias**:
    - Description: The GNodeAlias of the sender
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: The GNodeInstanceId of the sender
    - Format: UuidCanonicalTextual

**TimeUnixS**:
    - Description: Latest simulated time for sender. The time in unix seconds of the latest TimeStep received from the TimeCoordinator by the actor that sent the payload.

.. autoclass:: gwatn.types.ready.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwatn.types.ready.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.Ready_Maker
    :members:

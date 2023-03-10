GtDispatchBoolean
==========================
Python pydantic class corresponding to  json type ```gt.dispatch.boolean```.

.. autoclass:: gwatn.types.GtDispatchBoolean
    :members:

**AboutNodeName**:
    - Description: The Spaceheat Node getting dispatched
    - Format: LeftRightDot

**ToGNodeAlias**:
    - Description: GNodeAlias of the SCADA
    - Format: LeftRightDot

**FromGNodeAlias**:
    - Description: GNodeAlias of AtomicTNode
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: GNodeInstance of the AtomicTNode
    - Format: UuidCanonicalTextual

**RelayState**:
    - Description: 0 or 1

**SendTimeUnixMs**:
    - Description: Time the AtomicTNode sends the dispatch, by its clock
    - Format: ReasonableUnixTimeMs

.. autoclass:: gwatn.types.gt_dispatch_boolean.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwatn.types.gt_dispatch_boolean.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.gt_dispatch_boolean.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwatn.types.GtDispatchBoolean_Maker
    :members:

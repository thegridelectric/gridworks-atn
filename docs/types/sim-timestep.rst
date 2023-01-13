SimTimestep
==========================
Python pydantic class corresponding to  json type ```sim.timestep```.

.. autoclass:: gwatn.types.SimTimestep
    :members:

**FromGNodeAlias**:
    - Description: The GNodeAlias of the sender. The sender should always be a GNode Actor of role TimeCoordinator.
    - Format: LeftRightDot

**FromGNodeInstanceId**:
    - Description: The GNodeInstanceId of the sender
    - Format: UuidCanonicalTextual

**TimeUnixS**:
    - Description: Current time in unix seconds
    - Format: ReasonableUnixTimeS

**TimestepCreatedMs**:
    - Description: The real time created, in unix milliseconds
    - Format: ReasonableUnixTimeMs

**MessageId**:
    - Description: MessageId
    - Format: UuidCanonicalTextual

.. autoclass:: gwatn.types.sim_timestep.check_is_reasonable_unix_time_s
    :members:


.. autoclass:: gwatn.types.sim_timestep.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwatn.types.sim_timestep.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.sim_timestep.check_is_reasonable_unix_time_ms
    :members:


.. autoclass:: gwatn.types.SimTimestep_Maker
    :members:

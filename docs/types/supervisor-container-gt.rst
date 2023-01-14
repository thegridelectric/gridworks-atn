SupervisorContainerGt
==========================
Python pydantic class corresponding to  json type ```supervisor.container.gt```.

.. autoclass:: gwatn.types.SupervisorContainerGt
    :members:

**SupervisorContainerId**:
    - Description: Id of the docker SupervisorContainer
    - Format: UuidCanonicalTextual

**Status**:
    - Description:

**WorldInstanceName**:
    - Description: Name of the WorldInstance. For example, d1__1 is a potential name for a World whose World GNode has alias d1.
    - Format: WorldInstanceNameFormat

**SupervisorGNodeInstanceId**:
    - Description: Id of the SupervisorContainer's prime actor (aka the Supervisor GNode)
    - Format: UuidCanonicalTextual

**SupervisorGNodeAlias**:
    - Description: Alias of the SupervisorContainer's prime actor (aka the Supervisor GNode)
    - Format: LeftRightDot

.. autoclass:: gwatn.types.supervisor_container_gt.check_is_world_instance_name_format
    :members:


.. autoclass:: gwatn.types.supervisor_container_gt.check_is_uuid_canonical_textual
    :members:


.. autoclass:: gwatn.types.supervisor_container_gt.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.SupervisorContainerGt_Maker
    :members:

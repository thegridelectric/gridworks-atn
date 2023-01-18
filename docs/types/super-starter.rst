SuperStarter
==========================
Python pydantic class corresponding to  json type ```super.starter```.

.. autoclass:: gwatn.types.SuperStarter
    :members:

**SupervisorContainer**:
    - Description: Key data about the docker container

**GniList**:
    - Description: List of GNodeInstances (Gnis) run in the container

**AliasWithKeyList**:
    - Description: Aliases of Gnis that own Algorand secret keys
    - Format: LeftRightDot

**KeyList**:
    - Description: Algorand secret keys owned by Gnis

.. autoclass:: gwatn.types.super_starter.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.SuperStarter_Maker
    :members:

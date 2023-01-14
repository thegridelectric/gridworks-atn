HeartbeatAlgoAudit
==========================
Python pydantic class corresponding to  json type ```heartbeat.algo.audit```.

.. autoclass:: gwatn.types.HeartbeatAlgoAudit
    :members:

**FromGNodeAlias**:
    - Description: GNodeAlias of sender (AtomicTNode or Scada)
    - Format: LeftRightDot

**Heartbeat**:
    - Description: Heartbeat sender last sent to its partner

**SignedProof**:
    - Description: Tiny signed payment to DispatchContract to prove identity
    - Format: AlgoMsgPackEncoded

.. autoclass:: gwatn.types.heartbeat_algo_audit.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.heartbeat_algo_audit.check_is_algo_msg_pack_encoded
    :members:


.. autoclass:: gwatn.types.HeartbeatAlgoAudit_Maker
    :members:

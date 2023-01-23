HeartbeatAlgoAudit
==========================
Python pydantic class corresponding to  json type ```heartbeat.algo.audit```.

.. autoclass:: gwatn.types.HeartbeatAlgoAudit
    :members:

**SignedProof**:
    - Description: Tiny signed payment to DispatchContract to prove identity. Can be a minimal payment, as long as it comes from the AtomicTNode or SCADA.
    - Format: AlgoMsgPackEncoded

**Heartbeat**:
    - Description: Heartbeat sender last sent to its partner

.. autoclass:: gwatn.types.heartbeat_algo_audit.check_is_left_right_dot
    :members:


.. autoclass:: gwatn.types.heartbeat_algo_audit.check_is_algo_msg_pack_encoded
    :members:


.. autoclass:: gwatn.types.HeartbeatAlgoAudit_Maker
    :members:

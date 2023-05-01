

SDK for `gridworks-atn <https://pypi.org/project/gridworks-atn/>`_  Types
===========================================================================

The Python classes enumerated below provide an interpretation of gridworks-atn
type instances (serialized JSON) as Python objects. Types are the building
blocks for all GridWorks APIs. You can read more about how they work
`here <https://gridworks.readthedocs.io/en/latest/api-sdk-abi.html>`_, and
examine their API specifications `here <apis/types.html>`_.
The Python classes below also come with methods for translating back and
forth between type instances and Python objects.


.. automodule:: gwatn.types

.. toctree::
   :maxdepth: 1
   :caption: TYPE SDKS

    AcceptedBid  <types/accepted-bid>
    AtnBid  <types/atn-bid>
    AtnParams  <types/atn-params>
    BaseGNodeGt  <types/base-g-node-gt>
    BasegnodeScadaCreate  <types/basegnode-scada-create>
    DiscoverycertAlgoCreate  <types/discoverycert-algo-create>
    DispatchContractConfirmed  <types/dispatch-contract-confirmed>
    GNodeGt  <types/g-node-gt>
    GNodeInstanceGt  <types/g-node-instance-gt>
    GtDispatchBoolean  <types/gt-dispatch-boolean>
    GwCertId  <types/gw-cert-id>
    HeartbeatA  <types/heartbeat-a>
    HeartbeatAlgoAudit  <types/heartbeat-algo-audit>
    HeartbeatB  <types/heartbeat-b>
    InitialTadeedAlgoCreate  <types/initial-tadeed-algo-create>
    InitialTadeedAlgoOptin  <types/initial-tadeed-algo-optin>
    InitialTadeedAlgoTransfer  <types/initial-tadeed-algo-transfer>
    JoinDispatchContract  <types/join-dispatch-contract>
    LatestPrice  <types/latest-price>
    MarketSlot  <types/market-slot>
    MarketTypeGt  <types/market-type-gt>
    NewTadeedAlgoOptin  <types/new-tadeed-algo-optin>
    NewTadeedSend  <types/new-tadeed-send>
    OldTadeedAlgoReturn  <types/old-tadeed-algo-return>
    PriceQuantity  <types/price-quantity>
    PriceQuantityUnitless  <types/price-quantity-unitless>
    Ready  <types/ready>
    ScadaCertTransfer  <types/scada-cert-transfer>
    SimScadaDriverReport  <types/sim-scada-driver-report>
    SimTimestep  <types/sim-timestep>
    SlaEnter  <types/sla-enter>
    SuperStarter  <types/super-starter>
    SupervisorContainerGt  <types/supervisor-container-gt>
    TadeedSpecsHack  <types/tadeed-specs-hack>
    TavalidatorcertAlgoCreate  <types/tavalidatorcert-algo-create>
    TavalidatorcertAlgoTransfer  <types/tavalidatorcert-algo-transfer>
    TerminalassetCertifyHack  <types/terminalasset-certify-hack>

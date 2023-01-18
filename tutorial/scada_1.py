from algosdk.future.transaction import *
from beaker.client import ApplicationClient
from gridworks.dev_utils.algo_setup import dev_fund_to_min

import gwatn.config as config
from gwatn import DispatchContract
from gwatn.scada_actor import ScadaActor


scada = ScadaActor(config.ScadaSettings())
dev_fund_to_min(scada.acct.addr, 20)


scada.client.account_info(scada.acct.addr)

# confirm that it owns the SCADA Certificate
# and NOT an App

scada.initialize_dispatch_contract()

# IF it DOES own the app, get its number (5)

scada.dc_client = ApplicationClient(
    client=scada.client,
    app=DispatchContract(),
    signer=scada.acct.as_signer(),
    app_id=10,
)

scada.dc_client.get_application_state()

scada.dc_client.call(
    DispatchContract.hello,
    name="DispatchContract",
).return_value

scada.dc_client.call(
    DispatchContract.get_ta_alias,
).return_value

scada.dc_client.call(
    DispatchContract.hello,
    name="DispatchContract",
).return_value
import time

from gwatn.types import HeartbeatAlgoAudit_Maker
from gwatn.types import HeartbeatB_Maker


hb = HeartbeatB_Maker(
    from_g_node_alias=scada.alias,
    from_g_node_instance_id=scada.g_node_instance_id,
    my_hex="a",
    your_last_hex=0,
    last_received_time_unix_ms=int(1000 * (time.time() - 0.3)),
    send_time_unix_ms=int(1000 * time.time()),
).tuple

sp = scada.client.suggested_params()

from algosdk.atomic_transaction_composer import TransactionWithSigner


txn = PaymentTxn(
    sender=scada.acct.addr, sp=sp, receiver=scada.dc_client.app_addr, amt=1000
)


scada.dc_client.call(
    DispatchContract.heartbeat_algo_audit,
    signed_proof=TransactionWithSigner(txn, scada.acct.as_signer()),
    heartbeat=hb.as_dict(),
)

scada.dc_client.opt_in()

scada.client.account_info(scada.acct.addr)["created-apps"][0]["id"]

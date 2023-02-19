from algosdk.atomic_transaction_composer import TransactionWithSigner
from algosdk.future.transaction import *
from atn_actor import AtnActor
from beaker.client import ApplicationClient
from gridworks.dev_utils.algo_setup import dev_fund_to_min

import gwatn.config as config
from gwatn import DispatchContract


atn = AtnActor(config.AtnSettings())
dev_fund_to_min(atn.acct.addr, 20)


atn.dc_client = ApplicationClient(
    client=atn.client,
    app=DispatchContract(),
    signer=atn.acct.as_signer(),
    app_id=10,
)

atn.dc_client.get_application_state()


atn.dc_client.call(DispatchContract.hello, name="DispatchContract").return_value


sp = atn.dc_client.get_suggested_params()
sp.flat_fee = True
sp.fee = 2000
ptxn = PaymentTxn(atn.acct.addr, sp, atn.dc_client.app_addr, 100_000)

result = atn.dc_client.call(
    DispatchContract.bootstrap2,
    atn_seed=TransactionWithSigner(ptxn, atn.acct.as_signer()),
    TaTradingRights=4,
)

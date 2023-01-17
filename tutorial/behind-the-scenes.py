from algosdk.future.transaction import *
from algosdk.v2client.algod import AlgodClient
from gridworks.algo_utils import BasicAccount
from gridworks.dev_utils.algo_setup import dev_fund_to_min
from gridworks.gw_config import VanillaSettings


sk = "qUGjVDcxVa0TfV8IeL8ZG9FFROh/GzLaWS6Ie05jrHiLWHNvVZoPMX7bXlxHzGaJF9RAyueOoe1BXk+IUEBS2Q=="

gnf_admin = BasicAccount(sk)
dev_fund_to_min(gnf_admin.addr, 10)

settings = VanillaSettings()
client = AlgodClient(
    settings.algo_api_secrets.algod_token.get_secret_value(),
    settings.public.algod_address,
)

ta_alias = "d1.isone.ver.keene.holly.ta"
txn = AssetCreateTxn(
    sender=gnf_admin.addr,
    total=1,
    decimals=0,
    default_frozen=False,
    manager=gnf_admin.addr,
    asset_name=ta_alias,
    unit_name="SCADA",
    sp=client.suggested_params(),
)

signed_txn = txn.sign(gnf_admin.sk)
client.send_transaction(signed_txn)
client.account_info(gnf_admin.addr)

sp = client.suggested_params()

txn = AssetCreateTxn(
    sender=gnf_admin.addr,
    total=1,
    decimals=0,
    default_frozen=False,
    manager=gnf_admin.addr,
    asset_name=ta_alias,
    unit_name="TATRADE",
    sp=sp,
)


signed_txn = txn.sign(gnf_admin.sk)
client.send_transaction(signed_txn)

client.account_info(gnf_admin.addr)


###
# Transfer SCADA CERT to scada - first it opts in

from gwatn.config import ScadaSettings


sk = ScadaSettings().sk.get_secret_value()
scada_acct = BasicAccount(sk)

txn = AssetOptInTxn(
    sender=scada_acct.addr,
    index=3,
    sp=sp,
)
signed_txn = txn.sign(sk)
client.send_transaction(signed_txn)


# Then GNodeFactory can send
txn = AssetTransferTxn(
    sender=gnf_admin.addr, receiver=scada_acct.addr, amt=1, index=3, sp=sp
)
signed_txn = txn.sign(gnf_admin.sk)
client.send_transaction(signed_txn)

from gwatn.config import AtnSettings


sk = AtnSettings().sk.get_secret_value()
atn_acct = BasicAccount(sk)

txn = AssetOptInTxn(
    sender=atn_acct.addr,
    index=4,
    sp=client.suggested_params(),
)
signed_txn = txn.sign(sk)
client.send_transaction(signed_txn)

txn = AssetTransferTxn(
    sender=gnf_admin.addr, receiver=atn_acct.addr, amt=1, index=4, sp=sp
)
signed_txn = txn.sign(gnf_admin.sk)
client.send_transaction(signed_txn)

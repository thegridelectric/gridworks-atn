import logging

import gridworks.algo_utils as algo_utils
from algosdk.future.transaction import *
from gridworks.algo_utils import get_balances

from gwatn.scada_actor import ScadaActor


screen_handler = logging.StreamHandler()
fmt = "%(message)s"
screen_handler.setFormatter(logging.Formatter(fmt=fmt))
logging.getLogger().addHandler(screen_handler)
logging.getLogger().setLevel(logging.INFO)

from gwatn import DispatchContract


scada = ScadaActor()
scada.start()


# Things to try

scada.in_dispatch_contract()
scada.dc_client.get_application_state()


scada.dc_client.call(
    DispatchContract.hello,
    name="DispatchContract",
).return_value

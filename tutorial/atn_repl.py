import logging

from gridworks.algo_utils import get_balances

from gwatn.simple_atn_actor import SimpleAtnActor as Atn


screen_handler = logging.StreamHandler()
fmt = "%(message)s"
screen_handler.setFormatter(logging.Formatter(fmt=fmt))
logging.getLogger().addHandler(screen_handler)

atn = Atn()
atn.start()
client = atn.client
addr = atn.acct.addr


# various things you might run:
client.account_info(addr)

atn.hb_to_scada()

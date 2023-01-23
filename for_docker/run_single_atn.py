# docker exec -it atn bash
import logging

# from gwatn.strategies.heatpumpwithbooststore.atn import (
#     Atn__HeatPumpWithBoostStore as Atn
# )
from gwatn.simple_atn_actor import SimpleAtnActor as Atn


screen_handler = logging.StreamHandler()
fmt = "%(message)s"
screen_handler.setFormatter(logging.Formatter(fmt=fmt))
logging.getLogger().addHandler(screen_handler)


atn = Atn()

atn.start()

# docker exec -it atn bash
import logging
import sys

import dotenv
from pydantic import SecretStr

from gwatn.config import Settings
from gwatn.strategies.heatpumpwithbooststore.atn import (
    Atn__HeatPumpWithBoostStore as Atn,
)


settings = Settings(_env_file=dotenv.find_dotenv())
if len(sys.argv) < 5:
    raise Exception(f" Needs 4 inputs!")

settings.g_node_alias = sys.argv[1]
settings.g_node_id = sys.argv[2]
settings.g_node_instance_id = sys.argv[3]
settings.sk = SecretStr(sys.argv[4])

screen_handler = logging.StreamHandler()
fmt = "%(message)s"
screen_handler.setFormatter(logging.Formatter(fmt=fmt))
logging.getLogger().addHandler(screen_handler)


atn = Atn(settings=settings)

atn.start()

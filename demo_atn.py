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


screen_handler = logging.StreamHandler()
fmt = "%(message)s"
screen_handler.setFormatter(logging.Formatter(fmt=fmt))
logging.getLogger().addHandler(screen_handler)


atn = Atn(settings=settings)

atn.start()

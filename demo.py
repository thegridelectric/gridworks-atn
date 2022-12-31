import logging
import time
import dotenv

import gwatn.config as config


screen_handler = logging.StreamHandler()
fmt = "%(message)s"
screen_handler.setFormatter(logging.Formatter(fmt=fmt))
logging.getLogger().addHandler(screen_handler)

from gwatn.supervisor import SupervisorA


settings = config.SupervisorSettings(_env_file=dotenv.find_dotenv())

su = SupervisorA(settings=settings, size=4)
time.sleep(5)
su.start()

''' Script used to interface with an assistant model '''

import os
from pyassistant.config import init_config
from pyassistant.logger import init_logger
from pyassistant.diffuser_models.pixart_model import PixArtModel
from pyassistant.diffuser_models.pixart_model import PixArtModel_LowVRAM
from pyassistant.gui.main_window import init_main_window

config = init_config()
logger = init_logger(config["LOGGER"])

def start():
    main_window = init_main_window(config, logger)
    main_window.run()

if __name__ == "__main__":
    start()

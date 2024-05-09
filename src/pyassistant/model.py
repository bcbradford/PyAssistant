''' Wrapper class used to select a model '''

import gc
import torch
from pyassistant.diffuser_models.pixart_model import PixArtModel, PixArtModel_LowVRAM

class Model:

    def __init__(self, config, model_name, logger):
        self.__logger = logger
        self.__model = self.load_model(config, model_name, logger)
        self.model_type = config["TYPE"]
        
    def load_model(self, config, model_name, logger):
        match model_name:
            case "NLP_MODEL":
                pass
            case "PIXART_MODEL":
                return PixArtModel(config, logger)
            case "PIXART_MODEL_LOW_VRAM":
                return PixArtModel_LowVRAM(config, logger)
            case _:
                return None
        
    def generate(self, prompt):
        return self.__model.generate(prompt)

    def close(self):
        if self.model:
            self.__logger.info("Closing Model...")
            del self.model
            gc.collect()
            torch.cuda.empty_cache()
            self.model = None
            self.model_type = None
            self.__logger.info("Model Closed.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def init_model(config, model_name, logger):
    return DiffuserModel(config, model_name, logger)

''' Wrapper class for Pixart-α's PixArt-XL-2-1024-MS model '''

import torch
import gc
from transformers import T5EncoderModel
from diffusers import PixArtAlphaPipeline

class PixArtModel:

    def __init__(self, config, logger):
        self.__device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.__config = config
        self.__logger = logger
        self.__logger.info("Loading Model...")
        self.__pipe = PixArtAlphaPipeline.from_pretrained(config["MODEL"], 
                torch_dtype=torch.float16).to(self.__device)
        self.__logger.info("Loading Transformer...")
        self.__pipe.transformer = torch.compile(self.__pipe.transformer, 
                **config["TRANSFORMER_PARAMS"])
        self.__logger.info("Model Init Finished.")
    
    def generate(self, prompt):
        self.__logger.info("Generating Image...")
        image = self.__pipe(prompt=prompt).images[0]
        self.__logger.info("Image Generation Completed.")
        return image

class PixArtModel_LowVRAM:
    '''Manages GPU VRAM to avoid overflow'''

    def __init__(self, config, logger):
        self.__device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.__config = config
        self.__logger = logger

    def flush(self):
        gc.collect()
        torch.cuda.empty_cache()

    def generate(self, prompt):
        self.__logger.info("Loading Encoder...")
        self.__text_encoder = T5EncoderModel.from_pretrained(config["MODEL"],
                **self.__config["ENCODER_PARAMS"])
        
        self.__logger.info("Loading Model...")
        self.__pipe = PixArtAlphaPipeline.from_pretrained(
                "PixArt-alpha/PixArt-XL-2-1024-MS",
                text_encoder=self.__text_encoder,
                transformer=None,
                device_map="auto"
        )

        self.__logger.info("Generating Latent Params...")
        with torch.no_grad():
            latent_params = dict(zip([
                "prompt_embeds", 
                "prompt_attention_mask", 
                "negative_prompt_embeds", 
                "negative_prompt_attention_mask"
                ], self.__pipe.encode_prompt(prompt)))

        self.__logger.info("Cleaning Memory...")
        del self.__text_encoder
        del self.__pipe
        self.flush()

        self.__logger.info("Reloading Model...")
        self.__pipe = PixArtAlphaPipeline.from_pretrained(
                "PixArt-alpha/PixArt-XL-2-1024-MS",
                text_encoder=None,
                torch_dtype=torch.float16
        ).to(self.__device)

        self.__logger.info("Generating Latents...")
        latents = self.__pipe(
                negative_prompt=None,
                num_images_per_prompt=1,
                output_type="latent",
                **latent_params).images
        
        self.__logger.info("Cleaning Transformer...")
        del self.__pipe.transformer
        self.flush()

        self.__logger.info("Decoding Image...")
        with torch.no_grad():
            image = self.__pipe.vae.decode(latents / self.__pipe.vae.config.scaling_factor, 
                    return_dict=False)[0]
        
        self.__logger.info("Postprocessing Image...")
        image = self.__pipe.image_processor.postprocess(image, output_type="pil")[0]
        
        self.__logger.info("Removing Pipe...")
        del self.__pipe
        self.flush()

        self.__logger.info("Image Generation Completed.")
        return image

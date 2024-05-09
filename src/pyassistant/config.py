''' Module used to load the app's config '''

import os
import yaml
from dotenv import load_dotenv

def init_config() -> dict:
    package_path = os.path.dirname(os.path.dirname(__file__))
    project_path = os.path.dirname(package_path)
    config_path = os.path.join(project_path, "config.yml")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Path: '{project_path}' not found.")

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    if not config:
        raise Exception(f"Failed to load configuration from: {config_path}")

    # Set Paths
    config["OUTPUT_PATH"] = os.path.join(project_path, config["OUTPUT_PATH"])
    config["LOGGER"]["INFO_LOG"] = os.path.join(project_path, config["LOGGER"]["LOG_PATH"],
            config["LOGGER"]["INFO_LOG"])
    config["LOGGER"]["ERROR_LOG"] = os.path.join(project_path, config["LOGGER"]["LOG_PATH"],
            config["LOGGER"]["ERROR_LOG"])
    
    # Set Auth Token
    load_dotenv()
    config["AUTH_TOKEN"] = os.getenv("HUGGINGFACE_TOKEN")

    return config

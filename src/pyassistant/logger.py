'''
    Script that initializes a logger from python's standard logging module.
'''

import logging

def init_logger(config: dict) -> 'Logger':
    logger = logging.getLogger(config['NAME'])
    logger.setLevel(logging.DEBUG)

    info_handler = logging.FileHandler(config['INFO_LOG'])
    info_handler.setLevel(logging.INFO)

    error_handler = logging.FileHandler(config['ERROR_LOG'])
    error_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter(config['FORMAT'])
    
    info_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)

    return logger

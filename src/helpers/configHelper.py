import json
import os

with open(os.path.dirname(__file__) + '/../config/config.json') as data_file:
    CONFIG = json.load(data_file)

with open(os.path.dirname(__file__) + '/../config/levels.json') as data_file:
    LEVELS_CONFIG = json.load(data_file)

def get_config():
    return CONFIG

def get_level_config(mode, level_number):
    return LEVELS_CONFIG[mode + "-levels"][level_number - 1]

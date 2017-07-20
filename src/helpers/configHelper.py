import json
import os

with open(os.path.dirname(__file__) + '/../config/config.json') as data_file:
    CONFIG = json.load(data_file)

def get_config():
    return CONFIG

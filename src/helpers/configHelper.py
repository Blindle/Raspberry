import json
import os

with open(os.path.dirname(__file__) + '/../config/config.json') as data_file:
    CONFIG = json.load(data_file)

if os.path.exists('config/custom_levels.json'):
    with open(os.path.dirname(__file__) + '/../config/custom_levels.json') as data_file:
        print "Cargando niveles personalizados ..."
        LEVELS_CONFIG = json.load(data_file)
else:
    with open(os.path.dirname(__file__) + '/../config/levels.json') as data_file:
        print "Cargando niveles por default ..."
        LEVELS_CONFIG = json.load(data_file)

with open(os.path.dirname(__file__) + '/../config/symbols.config') as data_file:
    symbols_dict = dict()
    for line in data_file:
        fields = line.split("=")
        symbols_dict[fields[0]] = fields[1]
    SYMBOLS_CONFIG = symbols_dict

def get_config():
    return CONFIG

def get_level_config(mode, level_number):
    return LEVELS_CONFIG[mode + "-levels"][level_number - 1]

def get_symbol(key):
    return SYMBOLS_CONFIG[key]
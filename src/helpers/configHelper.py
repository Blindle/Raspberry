import json
import os

#with open(os.path.dirname(__file__) + '/../config/config.json') as data_file:
#    CONFIG = json.load(data_file)

#with open(os.path.dirname(__file__) + '/../config/levels.json') as data_file:
#    print "Cargando niveles por default ..."
#    LEVELS_CONFIG = json.load(data_file)

with open(os.path.dirname(__file__) + '/../config/symbols.config') as data_file:
    symbols_dict = dict()
    points_dict = dict()
    for line in data_file:
        fields = line.split("=")
        points = fields[0]
        symbol = fields[1].replace('\n', '').replace('\r', '')
        symbols_dict[points] = symbol
        points_dict[symbol] = points
    SYMBOLS_CONFIG = symbols_dict
    POINTS_CONFIG = points_dict

##FIXME: Hice esto para que me traiga dinamicamente los cambios en la configuracion.
# Ver si hay otra mejor manera de hacerlo 
def get_config():
    json_file = open(os.path.dirname(__file__) + '/../config/config.json')
    return json.load(json_file)

def get_level_config(mode, level_number):
    json_file = open(os.path.dirname(__file__) + '/../config/{}_levels.json'.format(get_config()["wordSource"]))
    levels_config = json.load(json_file)
    return levels_config[mode + "-levels"][level_number - 1]

def get_symbol(key):
    return SYMBOLS_CONFIG[key]

def get_points(symbol):
    return POINTS_CONFIG[symbol]

def update_system_config(key, value):
    system_config = get_config()
    system_config[key] = value

    config_file = open(os.path.dirname(__file__) + '/../config/config.json', 'w')
    config_file.write(json.dumps(system_config, indent=4, sort_keys=True))
    config_file.close()
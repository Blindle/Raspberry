import json

with open('./config/config.json') as data_file:
    config = json.load(data_file)

def getConfig():
    return config
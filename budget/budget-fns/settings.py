import configparser
from os.path import isfile

def get_config_default():
    config = configparser.ConfigParser()
    config.read_dict({"Basic": {
        "login": "", "password": "",
        "Device-ID" : "000000000000000",
        "Device-OS" : "Python3"
        }})
    return config
def write_config_file(config,filename = "settings.ini"):
    with open(filename,"w") as file:
        config.write(file)
def get_config_file(filename = "settings.ini"):
    if (isfile(filename)):
        config = configparser.ConfigParser()
        config.read(filename)
        return config
    else:
        return get_config_default()

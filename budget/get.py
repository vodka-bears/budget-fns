#!/usr/bin/python3

# Temporary script to be replaced with GUI 

from nalogru import get_receipt_nalogru
from requests import HTTPError, ConnectionError, RequestException
from settings import get_config_file, write_config_file
import default

def get_data(fn, fd, fpd):
    config = get_config_file()
    if (config["Basic"]["login"] == ""):
        # default.py is in .gitignore, use your own
        config["Basic"]["login"] = default.login
        config["Basic"]["password"] = default.password
        write_config_file(config)
    login = config["Basic"]["login"]
    password = config["Basic"]["password"]
    try:
        data=(get_receipt_nalogru(fn,fd,fpd,login,password))
    except ConnectionError:
        print("No Internet")
        return None
    except HTTPError:
        print("HTTP error")
        return None
    except RequestException:
        print("Data seems wrong")
        return None
    return data
#!/usr/bin/python3

import requests
from time import sleep

def get_receipt_nalogru(fn, fd, fpd, login, password):
    url = "http://proverkacheka.nalog.ru:8888/v1/inns/*/kkts/*/fss/" + str(fn)\
        + "/tickets/" + str(int(fd)) + "?fiscalSign=" + str(fpd) +\
        "&sendToEmail=no"
    headers = {"Device-Id": "000000000000000",
               "Device-OS": "Linux"
               }
    s = requests.Session()
    response = s.get(url, headers = headers,
                     auth = (login, password),)
    if (response.status_code == 202):
        sleep(5)
        response = s.get(url, headers = headers,
                     auth = (login, password))
    if (response.status_code == 202):
        raise requests.RequestException("Reciept not found")
    if (not response.ok):
        response.raise_for_status()
    return(response.json()["document"]["receipt"])

def verify_receipt_nalogru(fn,fd,fpd,paid_sum,date,optype):
        s = requests.Session()
        url = "http://proverkacheka.nalog.ru:8888/v1/ofds/*/inns/*/fss/"\
        + str(fn) + "/operations/" + str(optype) +\
        "/tickets/" + str(int(fd)) + "?fiscalSign="\
        + str(fpd) + "&date=" + date.strftime("%Y-%m-%dT%H:%M:%S") +\
        "&sum=" + str(int(paid_sum*100))
        response = s.get(url)
        if (response.status_code == 204):
            return True
        else:
            return False
        
        
        
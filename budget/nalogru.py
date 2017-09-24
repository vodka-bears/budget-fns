import requests
from time import sleep

def get_receipt_nalogru(fn, fd, fpd, login, password, deviceid, deviceos):
    url = "".join(["http://proverkacheka.nalog.ru:8888/v1/inns/*/kkts/*",
                   "/fss/{0}/tickets/{1}/?fiscalSign={2}&sendToEmail=no"])\
                   .format(str(fn), str(fd).lstrip("0"), str(fpd))
    headers = {"Device-Id": str(deviceid),
               "Device-OS": str(deviceos)
    }
    s = requests.Session()
    response = s.get(url, headers = headers,
                     auth = (login, password),)
    if (response.status_code == 202):
        sleep(5)
        response = s.get(url, headers = headers,
                     auth = (login, password))
    if (response.status_code == 202):
        raise requests.RequestException("Timed out")
    if (not response.ok):
        response.raise_for_status()
    return(response.json()["document"]["receipt"])

def verify_receipt_nalogru(fn,fd,fpd,paid_sum,date,optype):
        s = requests.Session()
        url = "".join(
            [
                "http://proverkacheka.nalog.ru:8888/v1/ofds/*/inns/*/", 
                "fss/{0}/operations/{1}/tickets/{2}?fiscalSign={3}",
                "&date={4}&sum={5}"
            ]).format(
                str(fn),
                str(optype),
                str(fd).lstrip("0"),
                str(fpd),
                date.strftime("%Y-%m-%dT%H:%M:%S"),
                str(int(paid_sum)*100)
        )
        response = s.get(url)
        if (response.status_code == 204):
            return True
        else:
            return False
        
        
        
#!/usr/bin/python3

import requests

def get_reciept_oneofd(fn,fd,fpd):
    main_url = "https://consumer.1-ofd.ru/"
    post_url = "https://consumer.1-ofd.ru/api/tickets/find-ticket"
    request_url = "https://consumer.1-ofd.ru/api/tickets/ticket/"
    useragent = "Mozilla/5.0 (X11; Linux x86_64) \
             AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
             Chromium/59.0.3071.86 Chrome/59.0.3071.86 Safari/537.36"
    s = requests.Session()
    s.headers = {"Connection":"keep-alive", "User-Agent":useragent,
                 "Accept": "text/html,application/xhtml+xml,application/xml;\
                 q=0.9,image/webp,image/apng,*/*;q=0.8",
                 "Accept-Encoding": "gzip, deflate, br",
                 "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4",
                 "Host": "consumer.1-ofd.ru",
                 "Upgrade-Insecure-Requests": "1",
                 "X-Compress": "null"}
    payload = {"fiscalDriveId": fn, "fiscalDocumentNumber":
               str(int(fd)), "fiscalId": fpd}
    s.get(main_url)
    s.headers.update(requests.utils.dict_from_cookiejar(s.cookies))
    s.headers["X-XSRF-TOKEN"] = s.headers.pop("XSRF-TOKEN")
    s.headers.pop("Upgrade-Insecure-Requests")
    headers_update = {"Accept": "application/json, text/plain, */*",
                      "Content-Type": "application/json;charset=UTF-8"}
    s.headers.update(headers_update)
    response = s.post(post_url, json = payload)
    if (response.json()["status"] != 1):
        raise requests.RequestException("Reciept not found")
    request_url = request_url + response.json()["uid"]
    out = s.get(request_url)
    return out.json()
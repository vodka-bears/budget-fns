#!/usr/bin/python3

import datetime

class Entry():
    def __init__(self,item):
        self.sum = float(item["sum"])/100
        self.price = float(item["price"])/100
        self.quantity = float(item["quantity"])
        self.name = item["name"]
        self.code = self.name.split(" ")[0]
        self.name = self.name[len(self.code) + 1:]
            

class Receipt():
    def __init__(self,data):
        self.rawdata = data
        self.paid_sum = float(data["totalSum"])/100
        self.items = []
        for item in data["items"]:
            self.items.append(Entry(item))
        self.sum = 0
        for item in self.items:
            self.sum += item.sum
        self.strtime = data["dateTime"]
        self.buytime = datetime.datetime.strptime(self.strtime,"%Y-%m-%dT%H:%M:%S")
        self.operator = data["operator"]
        self.user = data["user"]
        self.inn = data["userInn"]
        self.optype = data["operationType"]
        self.fn = data["fiscalDriveNumber"]
        self.fd = data["fiscalDocumentNumber"]
        self.fpd = data["fiscalSign"]
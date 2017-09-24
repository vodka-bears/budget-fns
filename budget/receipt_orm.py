import peewee
import datetime
from json import dumps

proxy = peewee.Proxy()

class BaseModel(peewee.Model):
    class Meta:
        database = proxy
            
class Receipt(BaseModel):
    rawdata_serial = peewee.TextField()
    paid_sum = peewee.FloatField()
    sum = peewee.FloatField()
    buytime = peewee.TimeField()
    operator = peewee.CharField()
    user = peewee.CharField()
    inn = peewee.CharField()
    optype = peewee.IntegerField()
    fn = peewee.IntegerField()
    fd = peewee.CharField()
    fpd = peewee.IntegerField(primary_key = True)
    def __init__(self,data):
        super(Receipt,self).__init__()
        self.rawdata = data
        self.rawdata_serial = dumps(self.rawdata, indent=4, sort_keys=True)
        self.paid_sum = float(data["totalSum"])/100
        self.items = []
        for item in data["items"]:
            self.items.append(Entry(item,self))
        self.sum = 0
        for item in self.items:
            self.sum += item.sum
        self.strtime = data["dateTime"]
        self.buytime = datetime.datetime.strptime(
            self.strtime,"%Y-%m-%dT%H:%M:%S"
        )
        self.operator = data["operator"]
        self.user = data["user"]
        self.inn = data["userInn"]
        self.optype = data["operationType"]
        self.fn = data["fiscalDriveNumber"]
        self.fd = data["fiscalDocumentNumber"]
        self.fpd = data["fiscalSign"]
    def save(self):
        for item in self.items:
            item.save()
        super(BaseModel,self).save(force_insert = True)
        
class Entry(BaseModel):
    sum = peewee.FloatField()
    price = peewee.FloatField()
    quantity = peewee.FloatField()
    name = peewee.CharField()
    barcode = peewee.CharField()
    nds10 = peewee.FloatField()
    nds18 = peewee.FloatField()
    receipt = peewee.ForeignKeyField(rel_model=Receipt, related_name="entries")
    def __init__(self,item,belongs):
        super(Entry,self).__init__()
        self.sum = float(item["sum"])/100
        self.price = float(item["price"])/100
        self.quantity = float(item["quantity"])
        self.name = item["name"]
        self.barcode = ""
        if "barcode" in item:
            self.barcode = item["barcode"]
        self.nds10 = 0
        self.nds18 = 0
        if "nds18" in item:
            self.nds18 = float(item["nds18"])/100
        if "nds10" in item:
            self.nds10 = float(item["nds10"])/100
        self.receipt = belongs
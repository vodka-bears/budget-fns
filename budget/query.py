from settings import get_config_file
from nalogru import verify_receipt_nalogru, get_receipt_nalogru
from receipt_orm import Receipt

class Query():
    def __init__(self, fn, fd, fpd, paid_sum, date, optype):
        self.fn = fn
        self.fd = fd
        self.fpd = fpd
        self.paid_sum = paid_sum
        self.date = date
        self.optype = optype
    def verify(self):
        self.response = verify_receipt_nalogru(
            self.fn,
            self.fd,
            self.fpd,
            self.paid_sum,
            self.date,
            self.optype
        )
        return self.response
    def get(self, login, password):
        config = get_config_file()
        deviceos = config["Basic"]["Device-OS"]
        deviceid = config["Basic"]["Device-Id"]
        response = get_receipt_nalogru(
            self.fn,
            self.fd,
            self.fpd,
            login,
            password,
            deviceid,
            deviceos
        )
        receipt = Receipt(response)
        return receipt
#!/usr/bin/python3

# A script used to test written functions, classess, etc.
# The same purpose as foo.py

from receipt import Receipt
from get import get_data
from nalogru import verify_receipt_nalogru


data = get_data(fn = "8710000100461774",
                fd = "0000013080", fpd = "4110138629")
if (data == None):
    print("fail")
    exit(1)
r = Receipt(data)
for item in r.items:
    print("%10s %32s %7.2f %7.3f %7.2f" %
          (item.code, item.name, item.price, item.quantity, item.sum))
print("Total: %.2f Rounded: %.2f" % (r.sum, r.paid_sum))
print(r.buytime.strftime("%d %B %Y, %H:%M"))
print(r.user)
print(r.inn)
print(r.operator)
ok = verify_receipt_nalogru(r.fn, r.fd, r.fpd, r.paid_sum, r.buytime, r.optype)
if ok:
    print("Verified")
else:
    print("Not verified")
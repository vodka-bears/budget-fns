#!/usr/bin/env python3

from scan import scan_code, parse_code
from settings import get_config_file
from json import dumps
import default

q = parse_code(scan_code("/dev/video0", (640,480)))

if q.verify():
    print("The receipt is verified")
else:
    print("FAKE RECEIPT")

r = q.get(default.login, default.password)

for item in r.items:
    print("%10s %32s %7.2f %7.3f %7.2f" %
          (item.barcode, item.name, item.price, item.quantity, item.sum))
print("Total: %.2f Paid: %.2f" % (r.sum, r.paid_sum))
print(r.buytime.strftime("%d %B %Y, %H:%M"))
print(r.user)
print(r.inn)
print(r.operator)
print(dumps(r.rawdata, indent=4, sort_keys=True))
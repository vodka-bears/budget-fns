#!/usr/bin/env python3

# A script used to test written functions, classess, etc.
# The same purpose as foo.py

from scan import scan_code, parse_code
from settings import get_config_file
import default

q = parse_code(scan_code("/dev/video0", (640, 480)))

if q.verify():
    print("The receipt is verified")
else:
    print("FAKE RECEIPT")

config = get_config_file()
deviceos = config["Basic"]["Device-OS"]
deviceid = config["Basic"]["Device-Id"]

r = q.get(default.login, default.password, deviceid, deviceos)

for item in r.items:
    print("%10s %32s %7.2f %7.3f %7.2f" %
          (item.code, item.name, item.price, item.quantity, item.sum))
print("Total: %.2f Paid: %.2f" % (r.sum, r.paid_sum))
print(r.buytime.strftime("%d %B %Y, %H:%M"))
print(r.user)
print(r.inn)
print(r.operator)

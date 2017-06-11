#!/usr/bin/python3

# A script used to test written functions, classess, etc.
# The same purpose as foo.py

from scan import scan_code, parse_code
import default

q = parse_code(scan_code("/dev/video0", (640,480)))

if q.verify():
    print("The reciept is verified")
else:
    print("FAKE RECIEPT")

r = q.get(default.login, default.password)

for item in r.items:
    print("%10s %32s %7.2f %7.3f %7.2f" %
          (item.code, item.name, item.price, item.quantity, item.sum))
print("Total: %.2f Rounded: %.2f" % (r.sum, r.paid_sum))
print(r.buytime.strftime("%d %B %Y, %H:%M"))
print(r.user)
print(r.inn)
print(r.operator)
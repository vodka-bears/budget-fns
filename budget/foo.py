#!/usr/bin/python3

# A script used to test written functions, classess, etc.
# The same purpose as dummy.py

from nalogru import verify_receipt_nalogru
from datetime import datetime

t = datetime
t = t.strptime("2017-06-08T19:54:00","%Y-%m-%dT%H:%M:%S")

correct = verify_receipt_nalogru(fn = "8710000100461774",
                           fd = "0000013080", fpd = "4110138629",
                           paid_sum = 364.00, date = t, optype = 1)
print(correct)
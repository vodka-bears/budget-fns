#!/usr/bin/env python3

# A script used to test written functions, classess, etc.
# The same purpose as dummy.py

from scan import scan_code, parse_code

code = scan_code("/dev/video0", (640, 480))
print(code)

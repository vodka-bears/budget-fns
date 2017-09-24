#!/usr/bin/env python3

from scan import scan_code, parse_code

code = scan_code("/dev/video0", (640, 480))
print(code)
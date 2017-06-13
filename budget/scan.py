# Based on: https://gist.github.com/snim2/255151

import pygame
import pygame.camera
from pygame.locals import *
import zbarlight
from PIL import Image
from urllib.parse import urlparse, parse_qs
from query import Query
from datetime import datetime

def scan_code(device, size):
    pygame.init()
    pygame.camera.init()
    display = pygame.display.set_mode(size, 0)
    pygame.display.set_caption("Scan QR-code here")
    camera = pygame.camera.Camera(device, size)
    camera.start()
    screen = pygame.surface.Surface(size, 0, display)
    capture = True
    while capture:
        screen = camera.get_image(screen)
        display.blit(screen, (0,0))
        pygame.display.flip()
        string = pygame.image.tostring(screen, "RGBA", False)
        image = Image.frombytes("RGBA", size, string)
        codes = zbarlight.scan_codes('qrcode', image)
        if codes:
            code = codes[0]
            capture = False
        for event in pygame.event.get():
            if event.type == QUIT:
                capture = False
    camera.stop()
    pygame.quit()
    code = str(code)
    code = code[2: len(code) - 1]
    return code

def parse_code(code):
    parsed = parse_qs(code)
    fn = parsed["fn"][0]
    fd = parsed["i"][0]
    fpd = parsed["fp"][0]
    paid_sum = float(parsed["s"][0])
    optype = int(parsed["n"][0])
    strdate = parsed["t"][0]
    if len(strdate) > 13:
        strdate = strdate[0:13]
    date = datetime.strptime(strdate, "%Y%m%dT%H%M")
    q = Query(fn, fd, fpd, paid_sum, date, optype)
    return q
    
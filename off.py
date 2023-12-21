#!/usr/bin/python3

# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./ledloop.py

import globals as gls

for pixel in gls.pixelSceneList:
    pixel.fill(0,0,0)

exit(0)

#!/usr/bin/python3

"""
Saves images every 0.2s into `images/` folder.
"""


import time

from picamera2 import Picamera2, Preview

print("""camera.py - Saves images every 0.2s into `images/` folder.
 
Press Ctrl+C to exit!
 
""")

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
picam2.configure(preview_config)

picam2.start_preview(Preview.QTGL)

picam2.start()

i = 0
try:
    while True:
        picam2.capture_file("images/image_{i}.jpg")
        i += 1
except KeyboardInterrupt:
    pass

time.sleep(2)

picam2.close()
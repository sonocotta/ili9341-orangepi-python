#!/usr/bin/env python3
import sys
import time

from PIL import Image
from OrangePi_ILI9341 import ILI9341

SPI_PORT = 0
SPI_CS = 0
SPI_DC = 27    # PA0
SPI_RES = 17   # PA1
BACKLIGHT = 22 # PA3

# Create TFT LCD display class.
disp = ILI9341(
    height=320,
    width=240,
    rotation=90,
    port=SPI_PORT,
    cs=SPI_CS,
    dc=SPI_DC,
    rst=SPI_RES,
    backlight=BACKLIGHT,
    spi_speed_hz=80 * 1000 * 1000,
    offset_left=0,
    offset_top=0
)

# Initialize display.
disp.begin()

# Load an image.
print('Loading image...')
image = Image.open('./examples/cat.jpg')

# Resize the image and rotate it so it's 240x320 pixels.
# image = image.rotate(90).resize((240, 320))

print('Press Ctrl-C to exit')
while(True):
    # Draw the image on the display hardware.
    print('Drawing image')
    start_time = time.time()
    disp.display(image)
    end_time = time.time()
    print('Time to draw image: ' + str(end_time - start_time))
    # disp.clear((0, 0, 0))
    # disp.display()

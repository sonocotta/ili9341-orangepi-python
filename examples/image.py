#!/usr/bin/env python3
import sys

from PIL import Image
from OrangePi_ILI9341 import ILI9341

SPI_PORT = 0
SPI_CS = 0
SPI_DC = 27    # PA0
SPI_RES = 17   # PA1
BACKLIGHT = 22 # PA3

# Create TFT LCD display class.
disp = ILI9341(
    # height=240,
    # width=320,
    # rotation=0,
    port=SPI_PORT,
    cs=SPI_CS,
    dc=SPI_DC,
    rst=SPI_RES,
    backlight=BACKLIGHT,
    # spi_speed_hz=60 * 1000 * 1000,
    # offset_left=0,
    # offset_top=0
)

# Initialize display.
disp.begin()

# Load an image.
print('Loading image...')
image = Image.open('./examples/cat.jpg')

# Resize the image and rotate it so it's 240x320 pixels.
# image = image.rotate(90).resize((240, 320))

# Draw the image on the display hardware.
print('Drawing image')
disp.display(image)

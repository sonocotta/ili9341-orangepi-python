# Python ILI9341 for OrangePi

Python library to control ILI9341 TFT LCD displays on the Orange Pi.

Designed to work with the following ILI9341 based SPI breakouts and Orange Pi Extension:

- [Orange PI Hi-Fi Hat](https://sonocotta.com/orange-pi-hi-fi-hat/)

# Installation

First, make sure you have the following dependencies:

````bash
sudo apt update
sudo apt install python3-spidev python3-pip python3-pil python3-numpy
````

Install this library by running:

````bash
sudo pip3 install OrangePi.ILI9341
````

You will also need to make sure SPI are enabled in armbian-config (`sudo armbian-config`) - you can find them under Interface Options. 

# Examples

You can find some examples of use in the examples folder. Clone this repo with:

```bash
git clone https://github.com/sonocotta/ili9341-orangepi-python
```

and navigate into the examples folder with:

```bash
cd ~/ili9341-orangepi-python/examples/
```

```bash
python3 shapes.py
```

# Licensing & History

This library is a modification of a modification of code originally written by Tony DiCola for Adafruit Industries, and modified to work with the ILI9341 by Clement Skau.

To create this ILI9341 driver, it has been hard-forked from st7735-python which was originally modified by Pimoroni to include support for their 160x80 SPI LCD breakout.

## Modifications include:

* PIL/Pillow has been removed from the underlying display driver to separate concerns- you should create your own PIL image and display it using `display(image)`
* `width`, `height`, `rotation`, `invert`, `offset_left` and `offset_top` parameters can be passed into `__init__` for alternate displays
* `Adafruit_GPIO` has been replaced with `OPi.GPIO` and `spidev` to closely align with our other software (IE: Orange Pi only)

Modified from 'Adafruit Python ILI9341' written by Tony DiCola for Adafruit Industries.'

MIT license, all text above must be included in any redistribution

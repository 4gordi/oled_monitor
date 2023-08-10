#!/usr/bin/env python3

import adafruit_ssd1306
import board
from PIL import Image, ImageDraw, ImageFont
import time

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

width = oled.width
height = oled.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

font = ImageFont.truetype('editundo.ttf', 30)

start_time = time.time()
timeout = 5

while time.time() < start_time + timeout:
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    for i in range(4):
    string_to_print = 'loading'+'.'*i

    draw.text((8, 20), string_to_print, font=font, fill='white')
    oled.image(image)
    oled.show()
    time.sleep(0.2)

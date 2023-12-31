#!/usr/bin/python3

import adafruit_ssd1306
import board
from PIL import Image, ImageDraw, ImageFont
import time
import datetime
import os
import busio
import subprocess
import sys

process = 'monitor.py'

try:
    output = subprocess.check_output(['pgrep', '-f', process])
    pid = int(output.strip())
    subprocess.run(['kill', str(pid)])
except subprocess.CalledProcessError:
    ans = process + ' is not found\n'
    sys.stdout.write(ans)

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

width = oled.width
height = oled.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

font = ImageFont.load_default()
font = ImageFont.truetype('editundo.ttf', 20)
mini_font = ImageFont.truetype('editundo.ttf', 16)

start_time = datetime.datetime.now()
timeout = 4

while True:
    time_left = timeout - (datetime.datetime.now() - start_time).total_seconds()
    if time_left < 1:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        oled.image(image)
        oled.show()
        break
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((25, 15), 'Power Off...', font=mini_font, fill=255)
    draw.text((10, 35), 'Time left: ' + str(int(time_left)), font=font, fill=255)
    oled.image(image)
    oled.show()
    time.sleep(1)

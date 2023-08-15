import time
import board
import busio
import digitalio
import os
import re

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Refresh
LOOPTIME = 1.0

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = oled.width
height = oled.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the >
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# Icons website: https://icons8.com/line-awesome
font = ImageFont.truetype('pixeloperator.ttf', 16)
icon_font= ImageFont.truetype('lineawesome-webfont.ttf', 18)

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/>
    #cmd = "hostname -I | cut -d\' \' -f1 | head --bytes -1"
    #IP = subprocess.check_output(cmd, shell = True)
    command = 'hostname -I'

    out = subprocess.getstatusoutput(command)
    ips = out[1]

    ips = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})').findall(ips)
    ips.append('pinas.local')

    #cmd = "df -h | awk '$NF==\"/\"{printf \"HDD: %d/%dGB %s\", $3,$2,$5}'"
    cmd = "df -h | awk '$NF==\"/\"{printf \"%d/%dGB\", $3,$2}'"
    MicroSD = subprocess.check_output(cmd, shell = True)

    cmd = "free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2}'"
    MemUsage = subprocess.check_output(cmd, shell = True)

    if os.path.exists('/dev/sda1'):
        cmd = "df -h | awk '$NF==\"/storage\"{printf \"%d/%d\", $3,$2}'"
        Disk1 = subprocess.check_output(cmd, shell = True)
        draw.text((x, top+25), chr(61600), font=icon_font, fill=255)
    else:
        Disk1 = subprocess.check_output("bash -c 'printf \"Fuck\"'", shell = True)
        draw.text((x, top+25), chr(63252), font=icon_font, fill=255)

    cmd = "vcgencmd measure_temp | cut -d '=' -f 2 | head --bytes -1"
    Temperature = subprocess.check_output(cmd, shell = True)

    # Icons
    # Icon temperature
    draw.text((x, top+5), chr(63339), font=icon_font, fill=255)
    # Icon memory
    draw.text((x+65, top+5), chr(62776), font=icon_font, fill=255)
    # Icon disk
    # draw.text((x, top+25), chr(61600), font=icon_font, fill=255)
    # Icon microsd
    draw.text((x+65, top+25), chr(63426), font=icon_font, fill=255)
    # Icon wifi
    draw.text((x, top+45), chr(61931), font=icon_font, fill=255)

    # Text
    # Text temperature
    draw.text((x+19, top+5), str(Temperature,'utf-8'),  font=font, fill=255)
    # Text memory usage
    draw.text((x+87, top+5), str(MemUsage,'utf-8'),  font=font, fill=255)
    # Text Disk usage
    draw.text((x+19, top+25), str(Disk1,'utf-8'),  font=font, fill=255)
    # Text MicroSD usage
    draw.text((x+87, top+25), str(MicroSD,'utf-8'), font=font, fill=255)
    # Text IP address
    #draw.text((x+19, top+45), str(IP,'utf-8'),  font=font, fill=255)
    for IP in ips:
        draw.rectangle((x+19,62,120,50), outline=0, fill=0)
        oled.image(image)
        oled.show()

        draw.text((x+19, top+45), str(IP),  font=font, fill=255)
        oled.image(image)
        oled.show()
        time.sleep(3)
    
    # Display image.
    oled.image(image)
    oled.show()

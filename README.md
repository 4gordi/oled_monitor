# python-scripts for oled screen (128x64)

sudo apt update && sudo apt upgrade

sudo apt install python3-pip

sudo pip3 install --upgrade setuptools

sudo apt-get install i2c-tools

sudo pip install smbus

sudo apt install git

cd ~

sudo pip3 install --upgrade adafruit-python-shell

wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py

sudo python3 raspi-blinka.py

sudo pip3 install adafruit-circuitpython-ssd1306

git clone https://github.com/4gordi/oled_monitor.git

cd oled_monitor

python3 monitor.py

crontab –e

sudo nano /etc/motd

@reboot cd /home/pi/oled_monitor && python3 loading.py && python3 monitor.py &

sudo nano /etc/systemd/system/shutdown.service

systemctl enable shutdown.service

systemctl status shutdown.service



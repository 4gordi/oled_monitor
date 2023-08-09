# oled_monitor
python-scripts for oled screen (128x64)

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

#sudo apt-get install python3-pil

git clone https://github.com/mklements/OLED_Stats.git

cd OLED_Stats

python3 stats.py

crontab –e

@reboot python3 /home/4gordi/stats.py &

cd OLED_Stats
cp PixelOperator.ttf ~/PixelOperator.ttf
cp stats.py ~/stats.py
cp fontawesome-webfont.ttf ~/fontawesome-webfont.ttf

@reboot cd /home/4gordi/OLED_Stats && python3 loading.py && python3 monitor.py &

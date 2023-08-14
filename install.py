#!/usr/bin/env python3

from adafruit_shell import Shell

shell = Shell()

shell.run_command("cd ~")

shell.run_command("sudo apt update && sudo apt upgrade")

shell.run_command("sudo apt install python3-pip")

shell.run_command("sudo pip3 install --upgrade setuptools")

shell.run_command("sudo apt-get install i2c-tools")

shell.run_command("sudo pip install smbus")

shell.run_command("sudo pip3 install --upgrade adafruit-python-shell")

shell.run_command("wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py")

shell.run_command("sudo python3 raspi-blinka.py")

shell.run_command("sudo pip3 install adafruit-circuitpython-ssd1306")

shell.run_command("sudo cp motd /etc/motd")

shell.run_command("sudo cp shutdown.service /etc/systemd/system/shutdown.service")

shell.run_command("systemctl enable shutdown.service")

shell.run_command("chmod +x crontab.sh")

shell.run_command("./crontab.sh")

shell.prompt_reboot()

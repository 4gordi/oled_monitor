#!/usr/bin/env python3

from adafruit_shell import Shell

shell = Shell()

shell.run_command("cd ~")

shell.run_command("sudo apt update && sudo apt upgrade -y")

shell.run_command("sudo apt-get install i2c-tools -y")

shell.run_command("sudo pip3 install --upgrade setuptools")

shell.run_command("sudo pip3 install smbus")

shell.run_command("sudo pip3 install adafruit-circuitpython-ssd1306")

shell.run_command("wget https://raw.githubusercontent.com/4gordi/oled_monitor/main/raspi-blinka.py")

shell.run_command("chmod +x raspi-blinka.py")

shell.run_command("sudo cp motd /etc/motd")

shell.run_command("sudo cp shutdown.service /etc/systemd/system/shutdown.service")

shell.run_command("systemctl enable shutdown.service")

shell.run_command("chmod +x crontab.sh")

shell.run_command("./crontab.sh")

shell.run_command("sudo reboot")

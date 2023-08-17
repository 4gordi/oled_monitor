#!/usr/bin/env python3

from adafruit_shell import Shell

shell = Shell()

shell.run_command("cd ~")

shell.run_command("sudo apt-get install -y python3-smbus i2c-tools")

shell.run_command("sudo pip3 install --upgrade setuptools")

shell.run_command("sudo pip3 install adafruit-circuitpython-ssd1306")

shell.run_command("cd oled_monitor/")

shell.run_command("chmod +x raspi-blinka.py")

shell.run_command("python3 raspi-blinka.py")

shell.run_command("sudo cp motd /etc/motd")

shell.run_command("sudo cp shutdown.service /etc/systemd/system/shutdown.service")

shell.run_command("sudo systemctl enable shutdown.service")

shell.run_command("chmod +x crontab.sh")

shell.run_command("./crontab.sh")

shell.run_command("sudo raspi-config nonint do_i2c 0")

shell.run_command("sudo reboot")

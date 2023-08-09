#!/usr/bin/python3

import subprocess

output = subprocess.check_output(['pgrep', '-f', 'monitor.py'])
pid = int(output.strip())
subprocess.run(['kill', str(pid)])

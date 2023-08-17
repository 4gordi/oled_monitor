#!/bin/bash

USERNAME=$(whoami)

#The new cron job
CRON_ADD="@reboot cd /home/$USERNAME/oled_monitor && python3 loading.py && python3 monitor.py &"

#Get crontab and remove lines containing "something" with sed
#CRON=$(crontab -u $USERNAME -l | sed -n "/something/!p")

#Make sure crontab ends with newline
if [ $(printf "$CRON" | tail -c 1 | wc -l) -eq 0 ]; then
  CRON="$CRON\n"
fi

#Modify the crontab
printf "$CRON$CRON_ADD\n" | crontab -u $USERNAME -


#!/bin/bash
# I got this script from john cambefort

# Script to start the train sign python program. Run this script should be run as the pi user.

# Forces running this script from the program's root directory (/home/pi/Tempo)
cd /home/pi/nyc-subway-sign

# Check to see whether the script is already running
if [ ! "$(screen -ls | grep -i 'trainsign')" ]; then
  # If not running, start it
  screen -d -m -S trainsign sudo python3 /home/pi/nyc-subway-sign/main.py
  echo "Turning on the sign by starting a new screen."
else
  echo "There is already a screen running."
fi

exit 0
#!/bin/bash

# this script stops the train sign python program
cd /home/pi/nyc-subway-sign

# Check to see whether the script is already running
if [ "$(screen -ls | grep -i 'trainsign')" ]; then
  # screen -r trainsign 
  echo "Turning off the sign by stopping the screen session."
  sudo reboot # TODO find a way to re-attach to the screen session (or just kill it)
else
  echo "No running script was found."
fi

exit 0
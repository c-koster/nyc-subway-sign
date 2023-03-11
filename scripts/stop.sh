#!/bin/bash

# this script stops the train sign python program
cd /home/pi/nyc-subway-sign

# Check to see whether the script is already running
if [ "$(screen -ls | grep -i 'trainsign')" ]; then
  screen -S trainsign -X stuff $'\003' # send the "trainsign" screen session CTRL-C
  echo "Turning off the sign by stopping the screen session."
else
  echo "No running script was found."
fi

exit 0
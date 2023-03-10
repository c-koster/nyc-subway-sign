# NYC Subway sign (🗽🍎🚉)


## Hardware Needed

## Pi Software Setup

Once the pi is wired, run the commands below. For the rpi-matrix setup, select the Adafruit HAT configuration.

```sh
sudo apt-get update
sudo apt-get install vim git tmux python3 python3-pip python3-dev python3-pillow -y
git clone https://github.com/c-koster/nyc-subway-sign
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/rgb-matrix.sh > rgb-matrix.sh
sudo bash rgb-matrix.sh
```



To turn on and off automatically, crontab needs the following entries (try `sudo crontab -e`):

```
0 8 * * *  sudo /home/pi/nyc-subway-sign/scripts/start.sh # START 8am every morning
0 22 * * * sudo /home/pi/nyc-subway-sign/scripts/stop.sh  # STOP 10pm every evening
# reboot to check for github changes
```

Add the following lines as environment variables (try `vim ~/.bashrc`):

```sh
export STATION_TO_TRACK="L11N"
export LINES_TO_TRACK="L"
```


## Notes & Errata

- MTA train signs list their destination next to the line-name. This changes dynamically if there is track maintinence. However I was not able to find an online resource w. So i went with uptown/downtown station names exracted from [stops.txt](./resources/stops.txt). Labels for the first and last station can be found in [line_ends.txt](./resources/line_ends.txt)
- 

## useful resources and people who have done the same thing

- https://pypi.org/project/underground/
- https://medium.com/@skalyani103/wheres-my-train-9c8431c76b7f 
- https://github.com/maxxscholten/nyc-train-sign 
- https://github.com/ty-porter/RGBMatrixEmulator/
- https://www.raspberrypi.com/news/nyc-train-sign/
- https://github.com/c-koster/tempo-mirror (private repo) contains example shell scripts for on/off switch and restart logic) 


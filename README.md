



## Pi Software Setup

```sh
sudo apt-get update
sudo apt-get install git tmux python3 python3-pip python3-dev python3-pillow -y
git clone https://github.com/c-koster/nyc-subway-sign
```


Need to edit the Makefile (swap regular with adafruit-hat) and run these commands to set up the matrix controller:
```
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)
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


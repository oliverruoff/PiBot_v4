# PiBot_v4
A small roboter based on a raspberry pi zero w, using lidar for locating.

## Setup

- Install python packages from requirements.txt
- Start pigpio demon on boot
    - `sudo systemctl enable pigpiod`
    - `sudo systemctl start pigpiod`
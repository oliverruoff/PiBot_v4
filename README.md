# PiBot_v4
A small roboter based on a raspberry pi zero w, using lidar for locating.

![Picture](docs/3d_real.png)

## First scans with the lidar

![lidar test](docs/lidar_test.png)
## Setup

- Install python packages from requirements.txt
- Start pigpio demon on boot
    - `sudo systemctl enable pigpiod`
    - `sudo systemctl start pigpiod`
- Enable serial mode P6 in interacing options (`sudo raspi-config`)

## Printable 3D objects
The robot is designed by myself, the printable 3d objects can be found in the [stls folder](stls/).

## Wiring

Also see [fritzing wiring](docs/PiBot_v4_wiring.fzz).

![Breadboard View](docs/wiring.png)

## Stepper

To connect the stepper motor to the driver and raspberry, refer to this [youtube video](https://www.youtube.com/watch?v=LUbhPKBL_IU&t=258s).  
Don't miss to adjust the motor driver, so you don't fry your motor. (set current to max. 71% of max. motor current, in this case 1.5A --> driver current max. 1.065A (0.71 x 1.5). You should be fine with around 0.7A). --> For the smaller stepper which moves the lidar on the top, I used 0.5A, since this stepper has an 1A rating.

### Stepper ramping

The robot will slip when accelerating from 0 to 100% speed instantly, so that's why I implemented a ramping function (can be called by setting `ramping` keyword to true in according stepper functions).

The ramping function uses following exponential function:

![expo function](docs/ramping_function.png)
(using desmos.com) for modeling the function.

## Hardware Used

- Raspberry Pi Zero W
- Stepper Motor + Driver (DRV8825) ( 12V 1.5A) x2
- Stepper Motor + Driver ( 5V ULN2003)
- Power Converter
- TF Luna mini Lidar
- Bosch 12v Battery Pack
- Switches x2
- Voltage meter

### DRV8825 wiring

In order to correctly wire the bigger stepper motors, also see this example wiring:

![drv wiring](docs/drv_wiring.jpg)

### TF-Luna 

Check the byte codes of the lidar sensor for implementation:
![tf-luna byte codes](docs/TF_Luna_Byte_Codes.png)

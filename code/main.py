from time import sleep

from actuators import stepper
from sensors import TFLUNA
from routines import test_all, recorder
from lidar import lidar
from combination import robot

import RPi.GPIO as GPIO

####################################
# Initializing sensors, motors, etc.
####################################

left_stepper = stepper.stepper(
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200, stepper_delay_seconds=0.0005, gpio_mode=GPIO.BCM)

right_stepper = stepper.stepper(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200, stepper_delay_seconds=0.0005, gpio_mode=GPIO.BCM)

top_stepper = stepper.stepper(
    DIR=6, STEP=26, SLP=13, RST=19, steps_per_revolution=200, stepper_delay_seconds=0.005, gpio_mode=GPIO.BCM)

tf_luna = TFLUNA.TFLuna()

robo = robot.Robot(left_stepper, right_stepper, top_stepper, tf_luna)

while True:
    inp = input("Input: "). split(" ")
    a = inp[0]
    if a == "1":
        top_stepper.make_one_step()
    elif a == "2":
        top_stepper.set_direction_clockwise(True)
    elif a == "3":
        top_stepper.set_direction_clockwise(False)
    elif a == "4":
        robo.drive_cm(int(inp[1]), bool(inp[2]))
    elif a == "5":
        robo.turn_degree(int(inp[1]), bool(inp[2]))
    elif a == "6":
        for _ in range(200):
            top_stepper.make_one_step()
    elif a == "7":
        print(lidar.scan_360_forth_and_back(top_stepper, tf_luna))
    elif a == "8":
        robo.start()
    elif a == "9":
        recorder.record(left_stepper, right_stepper)
    elif a == "10":
        robo.drive_cm(100, True, True)
    elif a == "11":
        robo.turn_degree(360, clockwise=True, ramping=True)

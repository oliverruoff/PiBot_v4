from functools import total_ordering
from time import sleep

from actuators import stepper
from sensors import tfluna
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

tfluna = tfluna.TFLuna()

robo = robot.Robot(left_stepper, right_stepper, top_stepper, tfluna)

while True:
    inp = input("Input: "). split(" ")
    a = inp[0]
    if a == "1":
        top_stepper.make_one_step()
    elif a == "2":
        # toggle top_stepper direction
        top_stepper.set_direction_clockwise(
            not top_stepper.is_direction_clockwise())
    elif a == "3":
        # drive top_stepper certain angle
        top_stepper.turn_stepper_angle(
            int(inp[1]), asynch=False, ramping=False)
    elif a == "4":
        # drive robot certain distance in cm
        robo.drive_cm(int(inp[1]), bool(inp[2]))
    elif a == "5":
        # turn robot certain angle in degree
        robo.turn_degree(int(inp[1]), bool(inp[2]))
    elif a == "6":
        recorder.record(left_stepper, right_stepper)
    elif a == "7":
        robo.start()
    elif a == "8":
        print(tfluna.read_tfluna_data())
    elif a == "9":
        top_stepper.deactivate_stepper()
        left_stepper.deactivate_stepper()
        right_stepper.deactivate_stepper()
    else:
        print("Command not recognized!")

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
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200, gpio_mode=GPIO.BCM)

right_stepper = stepper.stepper(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200, gpio_mode=GPIO.BCM)

top_stepper = stepper.stepper(
    DIR=6, STEP=26, SLP=13, RST=19, steps_per_revolution=200, gpio_mode=GPIO.BCM)

tf_luna = TFLUNA.TFLuna()

while True:
    a = input("Input: ")
    if a == "1":
        top_stepper.make_one_step()
    elif a == "2":
        top_stepper.set_direction_clockwise(True)
    elif a == "3":
        top_stepper.set_direction_clockwise(False)
    elif a == "4":
        top_stepper.turn_stepper_angle(360, False, False, False)
    elif a == "5":
        top_stepper.turn_stepper_angle(360, False)
    elif a == "6":
        for _ in range(200):
            top_stepper.make_one_step()
    elif a == "7":
        print(lidar.scan_360(top_stepper, tf_luna))
    elif a == "8":
        robo = robot.Robot(left_stepper, right_stepper, top_stepper, tf_luna)
        robo.start()
    elif a == "9":
        recorder.record(left_stepper, right_stepper)

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
        print(lidar.scan_360_forth_and_back(top_stepper, tfluna))
    elif a == "8":
        robo.start()
    elif a == "9":
        recorder.record(left_stepper, right_stepper)
    elif a == "10":
        robo.drive_cm(100, True, True)
    elif a == "11":
        robo.turn_degree(360, clockwise=True, ramping=False)
    elif a == "12":
        robo.turn_degree(1, True, True)
    elif a == "13":
        robo.turn_degree(5, True, True)
    elif a == "14":
        robo.turn_degree(10, True, True)
    elif a == "15":
        robo.turn_degree(100, True, True)
    elif a == "16":
        robo.turn_degree(300, True, True)
    elif a == "17":
        robo.turn_degree(int(inp[1]), True, True)
    elif a == "18":
        robo.drive_cm(80, forward=True, ramping=True)
        robo.turn_degree(90, clockwise=False, ramping=True)
        robo.drive_cm(50, forward=True, ramping=True)
        robo.turn_degree(90, clockwise=True, ramping=True)
        robo.drive_cm(50, forward=True, ramping=True)
        robo.turn_degree(90, clockwise=False, ramping=True)
        robo.drive_cm(300, forward=True, ramping=True)
        robo.turn_degree(360, clockwise=False, ramping=True)

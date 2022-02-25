from multiprocessing import Process

from actuators import stepper
from sensors import tfluna
from routines import test_all, recorder
from lidar import lidar
from combination import robot
from slam import slam

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
slam_ = slam.Slam()

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
    elif a == "10":
        cloud_1 = robo.lidar.scan_angle_with_stepper_position_reset(360)
        robo.drive_cm(50, forward=True)
        cloud_2 = robo.lidar.scan_angle_with_stepper_position_reset(360)
        moved_cloud = slam_.find_cloud_translation_and_rotation(cloud_1, cloud_2)[
            :-1]
        print(moved_cloud)
        print(moved_cloud[-1])
    elif a == "11":
        cloud_1 = robo.lidar.scan_angle_with_stepper_position_reset(360)
        cloud_2 = slam_.rotate_cloud(cloud_1, 90)
        print("____________________________________")
        print([(i[0], i[1]) for i in cloud_1])
        print("____________________________________")
        print(cloud_2)
    elif a == "12":
        cloud_1 = robo.lidar.scan_angle_with_stepper_position_reset(360)
        robo.drive_cm(50, forward=True)
        cloud_2 = robo.lidar.scan_angle_with_stepper_position_reset(360)
        cloud_3 = slam_.translate_cloud(cloud_2, 0, -50)
        print('Score 1:', slam_.score_2d_clouds(cloud_1, cloud_2))
        print('Score 2:', slam_.score_2d_clouds(cloud_1, cloud_3))
    else:
        print("Command not recognized!")

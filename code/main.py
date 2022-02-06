from time import sleep

from actuators import DRV8825
from sensors import TFLUNA
from routines import test_all, recorder
from lidar import lidar
from combination import robot

import RPi.GPIO as GPIO


left_stepper = DRV8825.DRV8825(
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200, gpio_mode=GPIO.BCM)

right_stepper = DRV8825.DRV8825(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200, gpio_mode=GPIO.BCM)

top_stepper = DRV8825.DRV8825(
    DIR=6, STEP=26, SLP=13, RST=19, steps_per_revolution=200, gpio_mode=GPIO.BCM)

tf_luna = TFLUNA.TFLuna()

# top_stepper.set_direction_clockwise(True)
#top_stepper.turn_stepper_angle(angle_in_degree=360, halfstep=False)
# top_stepper.set_direction_clockwise(False)
#top_stepper.turn_stepper_angle(angle_in_degree=360, halfstep=False)


# robo = robot.Robot(left_stepper, right_stepper, top_stepper, tf_luna)

# robo.start()

# recorder.record(left_stepper, right_stepper)

# top_stepper.turn_stepper_angle(360, False, ramp_up=False, ramp_down=False)

for _ in range(360):
    top_stepper.make_one_step()

# print(lidar.scan_360(top_stepper, tf_luna))

#
# while True:
#   tfluna_data = tf_luna.read_tfluna_data()
#   print('TFLuna data --> Distance:',
#         tfluna_data[0], '| Signal Strength:', tfluna_data[1], '| Sensor Temperatur:', tfluna_data[2])
#   sleep(0.5)


# left_stepper.turn_stepper_angle(828, True)
# right_stepper.turn_stepper_angle(828, True)

# test_all.test_top_stepper_and_bottom_steppers(
#    top_stepper, left_stepper, right_stepper)

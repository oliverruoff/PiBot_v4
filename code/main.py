from time import sleep

from actuators import DRV8825, ULN2003
from sensors import TFLUNA
from routines import test_all, recorder
from lidar import lidar

import RPi.GPIO as GPIO


left_stepper = DRV8825.DRV8825(
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200, gpio_mode=GPIO.BCM)

right_stepper = DRV8825.DRV8825(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200, gpio_mode=GPIO.BCM)

top_stepper = ULN2003.ULN2003(
    IN1=21, IN2=20, IN3=16, IN4=26, gpio_mode=GPIO.BCM)

tf_luna = TFLUNA.TFLuna()

# recorder.record(left_stepper, right_stepper)


print(lidar.scan_360(top_stepper, tf_luna))

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

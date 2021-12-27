from time import sleep

from actuators import DRV8825, ULN2003
from sensors import TFLUNA
from routines import test_all


left_stepper = DRV8825.DRV8825(
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200)

right_stepper = DRV8825.DRV8825(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200)

top_stepper = ULN2003.ULN2003(21, 20, 16, 26)

tf_luna = TFLUNA.TFLuna()

while True:
    tfluna_data = tf_luna.read_tfluna_data()
    print('TFLuna data --> Distance:',
          tfluna_data[0], '| Signal Strength:', tfluna_data[1], '| Sensor Temperatur:', tfluna_data[2])
    sleep(0.5)

test_all.test_top_stepper_and_bottom_steppers(
    top_stepper, left_stepper, right_stepper)

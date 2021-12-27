from actuators import DRV8825, ULN2003
from sensors import TFLUNA
from routines import test_all

left_stepper = DRV8825.DRV8825(
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200)

right_stepper = DRV8825.DRV8825(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200)

top_stepper = ULN2003.ULN2003(21, 20, 16, 26)

tf_luna = TFLUNA.TFLuna()

test_all.test_top_stepper_and_bottom_steppers(
    top_stepper, left_stepper, right_stepper)

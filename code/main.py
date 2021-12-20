import time

from actuators import DRV8825


left_Stepper = DRV8825.DRV8825(
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200)

right_Stepper = DRV8825.DRV8825(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200)

left_Stepper.set_direction(clockwise=False)
right_Stepper.set_direction(clockwise=True)

left_Stepper.run_continuously()
right_Stepper.run_continuously()

time.sleep(1)
left_Stepper.stop_continuous()
right_Stepper.stop_continuous()
time.sleep(1)
left_Stepper.run_continuously()
right_Stepper.run_continuously()

left_Stepper.set_direction(clockwise=True)
right_Stepper.set_direction(clockwise=False)

time.sleep(1)
left_Stepper.stop_continuous()
right_Stepper.stop_continuous()
time.sleep(1)
left_Stepper.run_continuously()
right_Stepper.run_continuously()

left_Stepper.set_direction(clockwise=True)
right_Stepper.set_direction(clockwise=True)

time.sleep(1)
left_Stepper.stop_continuous()
right_Stepper.stop_continuous()
time.sleep(1)
left_Stepper.run_continuously()
right_Stepper.run_continuously()

left_Stepper.set_direction(clockwise=False)
right_Stepper.set_direction(clockwise=False)

left_Stepper.stop_continuous()
right_Stepper.stop_continuous()

import time

from actuators import DRV8825, ULN2003


left_stepper = DRV8825.DRV8825(
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200)

right_stepper = DRV8825.DRV8825(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200)

top_stepper = ULN2003.ULN2003(21, 20, 16, 26)

top_stepper.turn_stepper_angle(360, True)

time.sleep(1)

top_stepper.turn_stepper_angle(360, False)

exit()

left_stepper.set_direction(clockwise=False)
right_stepper.set_direction(clockwise=True)

left_stepper.run_continuously()
right_stepper.run_continuously()

time.sleep(1)
left_stepper.stop_continuous()
right_stepper.stop_continuous()
time.sleep(1)
left_stepper.run_continuously()
right_stepper.run_continuously()

left_stepper.set_direction(clockwise=True)
right_stepper.set_direction(clockwise=False)

time.sleep(1)
left_stepper.stop_continuous()
right_stepper.stop_continuous()
time.sleep(1)
left_stepper.run_continuously()
right_stepper.run_continuously()

left_stepper.set_direction(clockwise=True)
right_stepper.set_direction(clockwise=True)

time.sleep(1)
left_stepper.stop_continuous()
right_stepper.stop_continuous()
time.sleep(1)
left_stepper.run_continuously()
right_stepper.run_continuously()

left_stepper.set_direction(clockwise=False)
right_stepper.set_direction(clockwise=False)

time.sleep(1)

left_stepper.stop_continuous()
right_stepper.stop_continuous()

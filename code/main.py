from actuators import DRV8825


left_Stepper = DRV8825.DRV8825(
    DIR=27, STEP=17, SLP=4, steps_per_revolution=200)

right_Stepper = DRV8825.DRV8825(
    DIR=12, STEP=25, SLP=24, steps_per_revolution=200)

left_Stepper.turn_stepper(720)
right_Stepper.turn_stepper(720)

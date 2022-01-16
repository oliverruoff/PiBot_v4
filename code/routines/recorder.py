def record(left_stepper, right_stepper):
    input = ""
    while input is not "z":
        input = input("Move >> ")
        if input == "w":
            left_stepper.set_direction(False)
            right_stepper.set_direction(True)
            left_stepper.turn_stepper_angle(360, True)
            right_stepper.turn_stepper_angle(360, True)
        elif input == "s":
            left_stepper.set_direction(True)
            right_stepper.set_direction(False)
            left_stepper.turn_stepper_angle(360, True)
            right_stepper.turn_stepper_angle(360, True)
        elif input == "a":
            left_stepper.set_direction(True)
            right_stepper.set_direction(True)
            left_stepper.turn_stepper_angle(207, True)
            right_stepper.turn_stepper_angle(207, True)
        elif input == "d":
            left_stepper.set_direction(False)
            right_stepper.set_direction(False)
            left_stepper.turn_stepper_angle(207, True)
            right_stepper.turn_stepper_angle(207, True)

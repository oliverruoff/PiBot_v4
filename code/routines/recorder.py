def record(left_stepper, right_stepper):
    input_ = ""
    while input_ is not "z":
        input_ = input("Move >> ")
        if input_ == "w":
            left_stepper.set_direction(False)
            right_stepper.set_direction(True)
            left_stepper.turn_stepper_angle(360, True)
            right_stepper.turn_stepper_angle(360, True)
        elif input_ == "s":
            left_stepper.set_direction(True)
            right_stepper.set_direction(False)
            left_stepper.turn_stepper_angle(360, True)
            right_stepper.turn_stepper_angle(360, True)
        elif input_ == "a":
            left_stepper.set_direction(True)
            right_stepper.set_direction(True)
            left_stepper.turn_stepper_angle(207, True)
            right_stepper.turn_stepper_angle(207, True)
        elif input_ == "d":
            left_stepper.set_direction(False)
            right_stepper.set_direction(False)
            left_stepper.turn_stepper_angle(207, True)
            right_stepper.turn_stepper_angle(207, True)
        elif input_ == "u":
            left_stepper.set_direction(False)
            right_stepper.set_direction(True)
            left_stepper.turn_stepper_angle(100, True)
            right_stepper.turn_stepper_angle(100, True)
        elif input_ == "j":
            left_stepper.set_direction(True)
            right_stepper.set_direction(False)
            left_stepper.turn_stepper_angle(100, True)
            right_stepper.turn_stepper_angle(100, True)
        elif input_ == "h":
            left_stepper.set_direction(True)
            right_stepper.set_direction(True)
            left_stepper.turn_stepper_angle(57, True)
            right_stepper.turn_stepper_angle(57, True)
        elif input_ == "k":
            left_stepper.set_direction(False)
            right_stepper.set_direction(False)
            left_stepper.turn_stepper_angle(57, True)
            right_stepper.turn_stepper_angle(57, True)
        left_stepper.activate_stepper()
        right_stepper.activate_stepper()

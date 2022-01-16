import json

recorded_movement = []


def record(left_stepper, right_stepper):
    input_ = ""
    while True:
        input_ = input("Move >> ")
        if input_ == "w":
            recorded_movement.append("w")
            play_movement(left_stepper, right_stepper, "w")
        elif input_ == "s":
            recorded_movement.append("s")
            play_movement(left_stepper, right_stepper, "s")
        elif input_ == "a":
            recorded_movement.append("a")
            play_movement(left_stepper, right_stepper, "a")
        elif input_ == "d":
            recorded_movement.append("d")
            play_movement(left_stepper, right_stepper, "d")
        elif input_ == "u":
            recorded_movement.append("u")
            play_movement(left_stepper, right_stepper, "u")
        elif input_ == "j":
            recorded_movement.append("j")
            play_movement(left_stepper, right_stepper, "j")
        elif input_ == "h":
            recorded_movement.append("h")
            play_movement(left_stepper, right_stepper, "h")
        elif input_ == "k":
            recorded_movement.append("k")
            play_movement(left_stepper, right_stepper, "w")
        elif input_ == "m":
            json_movement_list = json.dumps(recorded_movement)
            with open("saved_movement.json", "w") as text_file:
                text_file.write(json_movement_list)
            print("Saved List:")
            print(recorded_movement)
        elif input_ == "l":
            with open('saved_movement.json', 'r') as file:
                recorded_movement = file.read()
            print("Loaded list:")
            print(recorded_movement)
        elif input_ == "p":
            for movement in recorded_movement:
                play_movement(left_stepper, right_stepper, movement)
        elif input_ == "z":
            exit()


def play_movement(left_stepper, right_stepper, input_):
    if input_ == "w":
        left_stepper.set_direction(False)
        right_stepper.set_direction(True)
        left_stepper.turn_stepper_angle(360, True)
        right_stepper.turn_stepper_angle(360, True, True)
    elif input_ == "s":
        left_stepper.set_direction(True)
        right_stepper.set_direction(False)
        left_stepper.turn_stepper_angle(360, True)
        right_stepper.turn_stepper_angle(360, True, True)
    elif input_ == "a":
        left_stepper.set_direction(True)
        right_stepper.set_direction(True)
        left_stepper.turn_stepper_angle(207, True)
        right_stepper.turn_stepper_angle(207, True, True)
    elif input_ == "d":
        left_stepper.set_direction(False)
        right_stepper.set_direction(False)
        left_stepper.turn_stepper_angle(207, True)
        right_stepper.turn_stepper_angle(207, True, True)
    elif input_ == "u":
        left_stepper.set_direction(False)
        right_stepper.set_direction(True)
        left_stepper.turn_stepper_angle(100, True)
        right_stepper.turn_stepper_angle(100, True, True)
    elif input_ == "j":
        left_stepper.set_direction(True)
        right_stepper.set_direction(False)
        left_stepper.turn_stepper_angle(100, True)
        right_stepper.turn_stepper_angle(100, True, True)
    elif input_ == "h":
        left_stepper.set_direction(True)
        right_stepper.set_direction(True)
        left_stepper.turn_stepper_angle(57, True)
        right_stepper.turn_stepper_angle(57, True, True)
    elif input_ == "k":
        left_stepper.set_direction(False)
        right_stepper.set_direction(False)
        left_stepper.turn_stepper_angle(57, True)
        right_stepper.turn_stepper_angle(57, True, True)
    left_stepper.activate_stepper()
    right_stepper.activate_stepper()

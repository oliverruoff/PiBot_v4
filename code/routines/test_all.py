from time import sleep


def test_top_stepper_and_bottom_steppers(top_stepper, left_stepper, right_stepper):
    print('Turning left stepper 360°.')
    left_stepper.turn_stepper(360)
    print('Turning right stepper 360°.')
    right_stepper.turn_stepper(360)
    print('Switching stepper directions and reversing movement.')
    left_stepper.set_direction(False)
    right_stepper.set_direction(False)
    left_stepper.turn_stepper(360)
    right_stepper.turn_stepper(360)
    print('Checking continuous movement for 0.5s forward and back.')
    left_stepper.run_continuously()
    right_stepper.run_continuously()
    sleep(0.5)
    left_stepper.set_direction(True)
    right_stepper.set_direction(True)
    sleep(0.5)
    left_stepper.stop_continuous()
    right_stepper.stop_continuous()
    print('Checking top stepper 360° clockwise and ccw.')
    top_stepper.turn_stepper_angle(360)
    top_stepper.set_direction(False)
    top_stepper.turn_stepper_angle(360)
    print('Done')



class Robot:

    def __init__(self, left_stepper, right_stepper, top_stepper, tfluna):
        self.left_stepper = left_stepper
        self.right_stepper = right_stepper
        self.top_stepper = top_stepper
        self.tfluna = tfluna

        self.TYRE_CIRCUMFERENCE_CM = 28.9
        self.ROBOT_CIRCUMFERENCE_CM = 66.6

    def drive_cm(self, cm, forward):
        if forward:
            self.left_stepper.set_direction_clockwise(False)
            self.right_stepper.set_direction_clockwise(True)
        else:
            self.left_stepper.set_direction_clockwise(True)
            self.right_stepper.set_direction_clockwise(False)
        desired_angle = (cm / self.TYRE_CIRCUMFERENCE_CM) * 360
        self.left_stepper.turn_stepper_angle(desired_angle, True)
        self.right_stepper.turn_stepper_angle(desired_angle, True)

    def turn_degree(self, degree, clockwise):
        self.left_stepper.turn_stepper_angle(828, True)
        self.right_stepper.turn_stepper_angle(828, True)

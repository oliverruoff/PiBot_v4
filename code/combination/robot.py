

class Robot:

    def __init__(self, left_stepper, right_stepper, top_stepper, tfluna):
        self.left_stepper = left_stepper
        self.right_stepper = right_stepper
        self.top_stepper = top_stepper
        self.tfluna = tfluna

        self.TYRE_CIRCUMFERENCE_CM = 28.9
        self.ROBOT_CIRCUMFERENCE_CM = 66.6

    def drive_cm(self, cm, forward, ramp_up=True, ramp_down=True):
        if forward:
            self.left_stepper.set_direction_clockwise(False)
            self.right_stepper.set_direction_clockwise(True)
        else:
            self.left_stepper.set_direction_clockwise(True)
            self.right_stepper.set_direction_clockwise(False)
        desired_angle = (cm / self.TYRE_CIRCUMFERENCE_CM) * 360
        self.left_stepper.turn_stepper_angle(
            desired_angle, True, ramp_up, ramp_down)
        self.right_stepper.turn_stepper_angle(
            desired_angle, False, ramp_up, ramp_down)

    def turn_degree(self, degree, clockwise, ramp_up=True, ramp_down=True):
        if clockwise:
            self.left_stepper.set_direction_clockwise(False)
            self.right_stepper.set_direction_clockwise(False)
        else:
            self.left_stepper.set_direction_clockwise(True)
            self.right_stepper.set_direction_clockwise(True)

        desired_angle = (self.ROBOT_CIRCUMFERENCE_CM /
                         self.TYRE_CIRCUMFERENCE_CM) * degree
        self.left_stepper.turn_stepper_angle(
            desired_angle, True, ramp_up, ramp_down)
        self.right_stepper.turn_stepper_angle(
            desired_angle, False, ramp_up, ramp_down)

    def start(self):
        while True:
            dist = self.tfluna.read_distance() * 100
            print("Dist:", dist)
            if dist > 40:
                self.drive_cm(dist-30, True)
            else:
                self.turn_degree(90, True)

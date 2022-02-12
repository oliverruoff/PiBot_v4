from this import d
from lidar import lidar


class Robot:

    def __init__(self, left_stepper, right_stepper, top_stepper, tfluna):
        self.left_stepper = left_stepper
        self.right_stepper = right_stepper
        self.top_stepper = top_stepper
        self.tfluna = tfluna

        self.TYRE_CIRCUMFERENCE_CM = 28.9
        self.ROBOT_CIRCUMFERENCE_CM = 60.3
        self.TURNING_ERROR_MULTIPLIER = 1.083  # manually determined

    def drive_cm(self, cm, forward, ramping=True):
        if not forward:
            self.left_stepper.set_direction_clockwise(False)
            self.right_stepper.set_direction_clockwise(True)
        else:
            self.left_stepper.set_direction_clockwise(True)
            self.right_stepper.set_direction_clockwise(False)
        desired_angle = (cm / self.TYRE_CIRCUMFERENCE_CM) * \
            360 * self.TURNING_ERROR_MULTIPLIER
        self.left_stepper.turn_stepper_angle(
            desired_angle, True, ramping)
        self.right_stepper.turn_stepper_angle(
            desired_angle, False, ramping)

    def turn_degree(self, degree, clockwise, ramping=True):
        if clockwise:
            self.left_stepper.set_direction_clockwise(False)
            self.right_stepper.set_direction_clockwise(False)
        else:
            self.left_stepper.set_direction_clockwise(True)
            self.right_stepper.set_direction_clockwise(True)

        desired_angle = (self.ROBOT_CIRCUMFERENCE_CM /
                         self.TYRE_CIRCUMFERENCE_CM) * degree * self.TURNING_ERROR_MULTIPLIER
        self.left_stepper.turn_stepper_angle(
            desired_angle, True, ramping)
        self.right_stepper.turn_stepper_angle(
            desired_angle, False, ramping)

    def max_distance_routine(self):
        while True:
            env = lidar.scan_360(self.top_stepper, self.tfluna)
            max_dist = 0
            max_angle = 0
            for i in env:
                if i[2] > 800:
                    continue
                if i[2] > max_dist:
                    max_dist = i[2]
                    max_angle = i[3]
            dist_cm = max_dist
            # dist_cm = self.tfluna.read_distance() * 100
            print("Dist:", dist_cm, "at angle:", max_angle)
            if dist_cm > 40:
                self.turn_degree(max_angle, True)
                self.drive_cm(int(dist_cm/1.1), True)
            else:
                self.drive_cm(20, False)
                self.turn_degree(120, True)

    def start(self):
        self.top_stepper.activate_stepper()
        while True:
            distances = []
            self.top_stepper.set_direction_clockwise(False)
            for _ in range(25):
                self.top_stepper.make_one_step()
                distances.append(self.tfluna.read_distance() * 100)
            self.top_stepper.set_direction_clockwise(True)
            for _ in range(25):
                self.top_stepper.make_one_step()
            for _ in range(25):
                self.top_stepper.make_one_step()
                distances.append(self.tfluna.read_distance() * 100)
            self.top_stepper.set_direction_clockwise(False)
            for _ in range(25):
                self.top_stepper.make_one_step()
            distances = [i for i in distances if i != 0]
            dist_cm = min(distances)
            print('MIN DISTANCE: ', dist_cm)
            distances = []
            if dist_cm > 30:
                self.drive_cm(cm=10, forward=True, ramping=True)
            else:
                self.turn_degree(degree=45, clockwise=True, ramping=True)

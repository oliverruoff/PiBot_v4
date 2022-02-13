from lidar import lidar
import time


class Robot:

    def __init__(self, left_stepper, right_stepper, top_stepper, tfluna):
        self.left_stepper = left_stepper
        self.right_stepper = right_stepper
        self.top_stepper = top_stepper
        self.tfluna = tfluna

        self.position_X = 0
        self.position_Y = 0
        self.heading = 0

        self.TYRE_CIRCUMFERENCE_CM = 28.9              # manually determined
        self.ROBOT_CIRCUMFERENCE_CM = 60.3             # manually determined
        self.TURNING_ERROR_MULTIPLIER = 1.083          # manually determined
        self.TOP_STEPPER_CALIBRATION_DISTANCE_CM = 10  # manually determined
        self.TOP_STEPPER_CALIBRATION_OFFSET = 48       # manually determined

        self.lidar = lidar.lidar(top_stepper=top_stepper, tfluna=tfluna)

        # calibrating top_stepper (lidar) --> Bringing it to 0 position.
        self.calibrate_top_stepper()

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
        self.heading = (self.heading +
                        degree) % 360 if clockwise else (self.heading - degree) % -360

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

    def calibrate_top_stepper(self):
        """Setting the top stepper (lidar) to position 0, facing forwards, using the calibration pen.
        Since there are sometimes very small error readings, two consecutive readings have to be small.
        """
        print('Calibrating lidar.')
        self.top_stepper.set_direction_clockwise(clockwise=False)
        calibrated = False
        low_counter = 0
        while not calibrated:
            distance = self.tfluna.read_distance()
            print('Measured calibration distance:', distance)
            if distance < self.TOP_STEPPER_CALIBRATION_DISTANCE_CM and distance > 0:
                if low_counter == 2:
                    self.top_stepper.set_direction_clockwise(clockwise=True)
                    for _ in range(self.TOP_STEPPER_CALIBRATION_OFFSET):
                        self.top_stepper.make_one_step()
                    calibrated = True
                else:
                    low_counter += 1
            else:
                low_counter = 0
                self.top_stepper.make_one_step()
        print('Lidar calibrated!')

    def start(self):
        self.top_stepper.activate_stepper()
        while True:
            env_map = self.lidar.scan_angle_to_left_and_right(degree=45)
            distances = [i[2] for i in env_map if i[2] != 0]
            dist_cm = min(distances)
            print('MIN DISTANCE: ', dist_cm)
            distances = []
            if dist_cm > 40:
                self.left_stepper.set_direction_clockwise(True)
                self.right_stepper.set_direction_clockwise(True)
                self.left_stepper.run_continuously()
                self.right_stepper.run_continuously()
                while True:
                    dist = self.lidar.read_distance()
                    print('Distance in front of me:', dist)
                    if dist > 40:
                        time.sleep(0.1)
                    else:
                        break
                self.left_stepper.stop_continuous()
                self.right_stepper.stop_continuous()
                # self.drive_cm(cm=dist_cm-30, forward=True, ramping=True)
            else:
                self.turn_degree(degree=45, clockwise=True, ramping=True)
                print("My current heading:", self.heading)

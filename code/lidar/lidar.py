import RPi.GPIO as GPIO
import math


class lidar:

    def __init__(self, top_stepper, tfluna):
        self.top_stepper = top_stepper
        self.tfluna = tfluna

    def _get_coord(self, angle, distance):
        return round(math.sin(angle)*distance, 2), round(math.cos(angle)*distance, 2)

    def scan_angle_with_stepper_position_reset(self, degree, clockwise=True):
        """Scanning a desired angle and direction, then resets the steppers position.

        Args:
            degree (int): The desired angle to scan.
            clockwise (bool, optional): Clockwise if true, else counterclockwise. Defaults to True.

        Returns:
            list: [0] -> x | [1] -> y | [2] -> distance | [3] -> strength | [4] -> temperature | [5] angle
        """
        env_map = self._scan_angle(degree, clockwise)
        reverse = not clockwise
        self.top_stepper.set_direction_clockwise(clockwise=reverse)
        self.top_stepper.turn_stepper_angle(
            degree=degree, asynch=False, ramping=False)
        return env_map

    def scan_angle_to_left_and_right(self, degree):
        """Scans an angle to left (counterclockwise), then resets stepper position,
        then scans that angle to the right (clockwise), finally resetting stepper position.

        Args:
            degree (int): The angle in degree, the stepper should turn ccw and cw.

        Returns:
            list: [0] -> x | [1] -> y | [2] -> distance | [3] -> strength | [4] -> temperature | [5] angle
        """
        env_map = self.scan_angle_with_stepper_position_reset(
            degree=degree, clockwise=False)
        env_map += self.scan_angle_with_stepper_position_reset(
            degree=degree, clockwise=True)
        return env_map

    def scan_angle_forth_and_back(self, degree, clockwise):
        """
        Scans an angle with a direction and scans it again by resetting the steppers position.

        Args:
            degree (int): The angle in degree, the sensor should scan.

        Returns:
            list: [0] -> x | [1] -> y | [2] -> distance | [3] -> strength | [4] -> temperature | [5] angle
        """
        env_map = self._scan_angle(degree=degree, clockwise=clockwise)
        reverted_direction = not clockwise
        env_map += self._scan_angle(degree=degree,
                                    clockwise=reverted_direction)
        return env_map

    def _scan_angle(self, degree, clockwise=True):
        """Scans a certain angle and returns the collected data. 
        Note: This function will NOT reset the steppers position, use other
        functions for that (`scan_angle_with_stepper_position_reset`).

        Args:
            degree (int): Angle in degree to scan.
            clockwise (bool, optional): Direction of the scan. Defaults to True.

        Returns:
            list: [0] -> x | [1] -> y | [2] -> distance | [3] -> strength | [4] -> temperature | [5] angle
        """
        self.top_stepper.set_direction_clockwise(clockwise)
        env_map = []
        angle = 0 if clockwise else 360
        steps = int(self.top_stepper.steps_per_revolution / 360 * degree)
        for _ in range(steps):
            tfluna_data = self.tfluna.read_tfluna_data()
            distance = tfluna_data[0]
            print('Measured distance:', distance)
            angle = angle + 360/self.top_stepper.steps_per_revolution if clockwise else angle - \
                360/self.top_stepper.steps_per_revolution
            radians_angle = math.radians(angle)
            env_map.append(
                self._get_coord(radians_angle, distance) + (distance, tfluna_data[1], tfluna_data[2], angle))
            self.top_stepper.make_one_step()
        return env_map

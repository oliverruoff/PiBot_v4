import RPi.GPIO as GPIO
import math


class lidar:

    def __init__(self, top_stepper, tfluna):
        self.top_stepper = top_stepper
        self.tfluna = tfluna

    def get_coord(self, angle, distance, log=False):
        if log:
            print('>>>sin(', angle, ') =', math.sin(angle),
                  '*', distance, '=', math.sin(angle)*distance)
            print('>>>cos(', angle, ') =', math.cos(angle),
                  '*', distance, '=', math.cos(angle)*distance)
        return round(math.sin(angle)*distance, 2), round(math.cos(angle)*distance, 2)

    def scan_angle(self, degree, clockwise=True):
        env_map = self._scan_angle(degree, clockwise)
        reverse = not clockwise
        self.top_stepper.set_direction_clockwise(clockwise=reverse)
        self.top_stepper.turn_stepper_angle(
            degree=degree, asynch=False, ramping=False)
        return env_map

    def scan_angle_both_directions(self, degree):
        """Scanning a desired angle ccw, then returning to start position, then scanning 
        the desired angle cw finally bringing lidar back to start position.

        Args:
            degree (int): The angle in degree, the stepper should turn ccw and cw.

        Returns:
            list: [0] -> x | [1] -> y | [2] -> distance | [3] -> strength | [4] -> temperature | [5] angle
        """
        env_map = self._scan_angle(degree, clockwise=False)
        self.top_stepper.set_direction_clockwise(clockwise=True)
        self.top_stepper.turn_stepper_angle(
            degree=degree, asynch=False, ramping=False)
        env_map += self._scan_angle(degree, clockwise=True)
        self.top_stepper.set_direction_clockwise(clockwise=False)
        self.top_stepper.turn_stepper_angle(
            degree=degree, asynch=False, ramping=False)
        return env_map

    def scan_angle_forth_and_back(self, degree):
        """Generates a list with coordinates in cm, distance and angle.

        Args:
            degree (int): The angle in degree, the sensor should scan.

        Returns:
            list: List containing x, y, distance, angle
        """
        env_map = self._scan_angle(degree=degree, clockwise=True)
        env_map += self._scan_angle(degree=degree, clockwise=False)
        return env_map

    def _scan_angle(self, degree, clockwise=True):
        self.top_stepper.set_direction_clockwise(clockwise)
        env_map = []
        angle = 0 if clockwise else 360
        steps = self.top_stepper.steps_per_revolution / 360 * degree
        for _ in range(steps):
            distance = self.tfluna.read_tfluna_data()
            print('Measured distance:', distance)
            angle = angle + 360/self.top_stepper.steps_per_revolution if clockwise else angle - \
                360/self.top_stepper.steps_per_revolution
            print('Current angle:', angle)
            radians_angle = math.radians(angle)
            env_map.append(
                self.get_coord(radians_angle, distance) + (distance, angle))
            self.top_stepper.make_one_step()
        return env_map

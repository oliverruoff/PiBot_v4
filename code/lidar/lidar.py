import RPi.GPIO as GPIO
import math


def get_coord(angle, distance, log=False):
    if log:
        print('>>>sin(', angle, ') =', math.sin(angle),
              '*', distance, '=', math.sin(angle)*distance)
        print('>>>cos(', angle, ') =', math.cos(angle),
              '*', distance, '=', math.cos(angle)*distance)
    return round(math.sin(angle)*distance, 2), round(math.cos(angle)*distance, 2)


def scan_360(stepper, tfluna, clockwise=True):
    env_map = _scan_360(stepper, tfluna, clockwise)
    reverse = not clockwise
    stepper.set_direction_clockwise(reverse)
    stepper.run_stepper(200, False)
    return env_map


def scan_360_forth_and_back(stepper, tfluna):
    env_map = _scan_360(stepper, tfluna, True)
    env_map += _scan_360(stepper, tfluna, False)
    return env_map


def _scan_360(stepper, tfluna, clockwise=True):
    stepper.set_direction_clockwise(clockwise)
    env_map = []
    angle = 0 if clockwise else 360
    for i in range(200):
        distance = tfluna.read_distance() * 100  # converting to cm
        print('Measured distance:', distance)
        angle = angle + 360/200 if clockwise else angle - 360/200
        print('Current angle:', angle)
        radians_angle = math.radians(angle)
        env_map.append(get_coord(radians_angle, distance) + (distance, angle))
        stepper.run_stepper(1, False)
    return env_map

import RPi.GPIO as GPIO
import math


def get_coord(angle, distance, log=False):
    if log:
        print('>>>sin(', angle, ') =', math.sin(angle),
              '*', distance, '=', math.sin(angle)*distance)
        print('>>>cos(', angle, ') =', math.cos(angle),
              '*', distance, '=', math.cos(angle)*distance)
    return round(math.sin(angle)*distance), round(math.cos(angle)*distance)


def scan_360(stepper, tfluna, clockwise=True):
    stepper.set_direction(clockwise)
    env_map = []
    for angle in range(360):
        distance = tfluna.read_distance()
        radians_angle = math.radians(angle)
        env_map.append(get_coord(radians_angle, distance))
        stepper.turn_stepper_angle(1)
    reverse_direction = not clockwise
    stepper.set_direction(reverse_direction)
    stepper.turn_stepper_angle(360)
    return env_map

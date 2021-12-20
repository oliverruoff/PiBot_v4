from time import sleep
import RPi.GPIO as GPIO

DIR = 12   # Direction GPIO Pin
STEP = 25  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 1.8) (1,8° per step (oruoff))
STEPPER_ACTIVATION_PIN = 24  # If set to Low, there is no holding torque on the motor


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(STEPPER_ACTIVATION_PIN, GPIO.OUT)

GPIO.output(DIR, CW)
delay = .0005


def turn_stepper(degree, clockwise=True):
    GPIO.output(STEPPER_ACTIVATION_PIN, GPIO.HIGH)
    direction = CCW
    if clockwise:
        direction = CW
    GPIO.output(DIR, direction)
    for _ in range(int(SPR/360*degree)):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    GPIO.output(STEPPER_ACTIVATION_PIN, GPIO.LOW)


def toggle_stepper(degree, repetitions, delay, start_clockwise=True):
    clockwise = start_clockwise
    for _ in range(repetitions):
        for __ in range(2):
            turn_stepper(degree, clockwise)
            clockwise = False if clockwise else True
            sleep(delay)

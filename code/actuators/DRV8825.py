from time import sleep
import RPi.GPIO as GPIO

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation


class DRV8825:

    def __init__(self, DIR, STEP, SLP, steps_per_revolution, stepper_delay=.0005, gpio_mode=GPIO.BCM):
        self.DIR = DIR
        self.STEP = STEP
        # If set to Low, there is no holding torque on the motor
        self.SLP = SLP
        # Steps per Revolution (360 / 1.8) (1,8° per step (oruoff))
        self.SPR = steps_per_revolution

        self.stepper_delay = stepper_delay
        self.gpio_mode = gpio_mode

        GPIO.setmode(gpio_mode)

        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.SLP, GPIO.OUT)

        GPIO.output(DIR, CW)

    def turn_stepper(self, degree, clockwise=True):
        GPIO.output(self.SLP, GPIO.HIGH)
        direction = CCW
        if clockwise:
            direction = CW
        GPIO.output(self.DIR, direction)
        for _ in range(int(self.SPR/360*degree)):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.stepper_delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.stepper_delay)
        GPIO.output(self.SLP, GPIO.LOW)

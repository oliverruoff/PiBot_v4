from time import sleep
import RPi.GPIO as GPIO
import pigpio

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

        self.pi = pigpio.pi()

        self.direction = CW

        GPIO.setmode(gpio_mode)

        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.SLP, GPIO.OUT)

        GPIO.output(DIR, CW)

    def activate_stepper(self):
        GPIO.output(self.SLP, GPIO.HIGH)

    def deactivate_stepper(self):
        GPIO.output(self.SLP, GPIO.LOW)

    def run_continuously(self, dutycycle=128, frequency=500):
        self.pi.set_PWM_dutycycle(self.STEP, dutycycle)
        self.pi.set_PWM_frequency(self.STEP, frequency)

    def stop_continuous(self):
        self.pi.set_PWM_dutycycle(self.STEP, 0)

    def set_direction(self, clockwise=True):
        self.direction = CW if clockwise else CCW
        GPIO.output(self.DIR, self.direction)

    def turn_stepper(self, degree):
        self.activate_stepper()
        for _ in range(int(self.SPR/360*degree)):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.stepper_delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.stepper_delay)
        self.deactivate_stepper()

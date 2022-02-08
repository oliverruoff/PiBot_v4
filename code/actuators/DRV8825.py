from multiprocessing.connection import wait
from time import sleep
import threading

import RPi.GPIO as GPIO
import pigpio

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation


class DRV8825:
    """This class is for handling the DRV8825 motor driver. E.g. to operate
        common bigger stepper motors.
        """

    def __init__(self, DIR, STEP, SLP, steps_per_revolution, RST=None, stepper_delay_seconds=.002, gpio_mode=GPIO.BCM):
        self.DIR = DIR
        self.STEP = STEP
        self.RST = RST
        # If set to Low, there is no holding torque on the motor
        self.SLP = SLP
        # Steps per Revolution (360 / 1.8) (1,8° per step (oruoff))
        self.SPR = steps_per_revolution

        self.stepper_delay_seconds = stepper_delay_seconds
        self.gpio_mode = gpio_mode

        self.pi = pigpio.pi()

        self.direction = CW

        GPIO.setmode(gpio_mode)

        if RST is not None:
            GPIO.setup(self.RST, GPIO.OUT)
            GPIO.output(self.RST, GPIO.HIGH)

        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.SLP, GPIO.OUT)

        GPIO.output(DIR, CW)

    def set_stepper_delay(self, stepper_delay_seconds):
        """Sets the delay in seconds for the driver to wait between steps.

        Args:
            stepper_delay_seconds (float): Delay in seconds to wait between steps.
        """
        self.stepper_delay_seconds = stepper_delay_seconds

    def activate_stepper(self):
        """Activates the stepper, which also will put holding torque on the stepper.
        This is required in order to move the stepper.
        """
        GPIO.output(self.SLP, GPIO.HIGH)

    def deactivate_stepper(self):
        """Deactivates the stepper and also releases holding torque on the stepper.
        In a deactivated state, the stepper will not be able to move.
        """
        GPIO.output(self.SLP, GPIO.LOW)

    def run_continuously(self, dutycycle=128, frequency=320):
        """Activated, the stepper will continuously run with the desired frequency.
        The dutycycle describes the distribution of high low states, where 128 is 50% / 50% high / low.

        Args:
            dutycycle (int, optional): Describes high / low ratio. 128 is 50%/50%. Defaults to 128.
            frequency (int, optional): Describes the frequency of the stepper's high / low states. Defaults to 320.
        """
        self.activate_stepper()
        self.pi.set_PWM_dutycycle(self.STEP, dutycycle)
        self.pi.set_PWM_frequency(self.STEP, frequency)

    def stop_continuous(self):
        """Stops the continuous turning of the stepper. Also deactivates it, thus
        releasing holding torque.
        """
        self.deactivate_stepper()
        self.pi.set_PWM_dutycycle(self.STEP, 0)

    def set_direction_clockwise(self, clockwise=True):
        """Sets the spinning direction of the stepper motor to clockwise or
        counterclockwise.

        Args:
            clockwise (bool, optional): Spinning direction. Defaults to True.
        """
        self.direction = CW if clockwise else CCW
        GPIO.output(self.DIR, self.direction)

    def turn_stepper_angle(self, degree, asynch, ramp_up=True, ramp_down=True):
        """Turns the stepper for a precise angle. Can be called
        either synchronous or asynchronously.

        Args:
            degree (int): The angle in degree, on how much the stepper will
            rotate.
            asynch (bool): Flag wheather this function (and therefore the motor), will turn
            synchronously or asynchronously.
        """
        if (asynch):
            thread = threading.Thread(
                target=self._turn_stepper, args=([degree, ramp_up, ramp_down]), kwargs={})
            thread.start()
        else:
            self._turn_stepper(degree, ramp_up, ramp_down)

    def _turn_stepper(self, degree, ramp_up=True, ramp_down=True):
        """This function is for turning the stepper for a precise angle.
        This function should be called with the `turn_stepper_angle` function,
        defining whether the function should run synchronously or asynchronously.

        Args:
            degree (int): The angle in degree, on how much the stepper will rotate.
            ramp_up (bool): Defines wheather the stepper should ramp up the movement.
            ramp_down (bool): Defines wheather the stepper should ramp down the movement.
        """
        self.activate_stepper()
        steps = int(self.SPR/360*degree)
        # means 1/5 of the beginning steps will be ramp up phase and the last 1/5 of the steps is ramp down phase
        ramp_size = 4
        ramp_steps = steps / ramp_size
        max_delay = self.stepper_delay_seconds * 10
        delay = 0
        if ramp_up:
            delay = max_delay
        for i in range(steps):
            if ramp_up:
                if i < ramp_steps:
                    delay -= (1/ramp_steps) * max_delay
            if ramp_down:
                if i > steps - ramp_steps:
                    delay += (1/ramp_steps) * max_delay
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.stepper_delay_seconds + delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.stepper_delay_seconds + delay)
        self.deactivate_stepper()

    def make_one_step(self):
        GPIO.output(self.STEP, GPIO.HIGH)
        sleep(self.stepper_delay_seconds)
        GPIO.output(self.STEP, GPIO.LOW)
        sleep(self.stepper_delay_seconds)

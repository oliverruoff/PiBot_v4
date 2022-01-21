import RPi.GPIO as GPIO
import time

# Sequence needed to operate the stepper
HALFSTEP_SEQ = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

FULLSTEP_SEQ = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1]
]


class ULN2003:
    """This class is for handling the ULN2003 stepper driver. E.g. to operate common
    small, low budget stepper motors.
    """

    def __init__(self, IN1, IN2, IN3, IN4, steps_per_revolution, gpio_mode=GPIO.BCM):
        GPIO.setmode(gpio_mode)
        self.stepper_pins = [IN1, IN2, IN3, IN4]

        # Initializing pins
        for pin in self.stepper_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        self.direction_clockwise = True
        self.steps_per_revolution = steps_per_revolution

    def run_stepper(self, steps, stepper_delay=0.001, halfstep=True):
        """Runs the stepper motor for the given number of steps.
        Note, that "clockwise" depends on pin setup.
        512 steps == 1 round for smaller, 200 steps == 1 round for bigger stepper.
        Arguments:
            steps {int} -- Number of steps the motor will do.
        Keyword Arguments:
            stepper_delay {float} -- Defines the time to wait between steps. (default: {0.001})
            halfstep {bool} -- Defines wheather to use half steps or fullsteps (default: {True})
        """

        if halfstep:
            seq = HALFSTEP_SEQ
            step_range = range(
                8) if not self.direction_clockwise else list(reversed(range(8)))
        else:
            seq = FULLSTEP_SEQ
            step_range = range(
                4) if not self.direction_clockwise else list(reversed(range(4)))
        for _ in range(steps):
            for step in step_range:
                for pin in range(4):
                    GPIO.output(
                        self.stepper_pins[pin], seq[step][pin])
                time.sleep(stepper_delay)

    def set_direction_clockwise(self, clockwise):
        """Sets the spinning direction of the stepper motor.

        Args:
            clockwise (bool): The spinning direction of the stepper motor. True = clockwise
        """
        self.direction_clockwise = clockwise

    def turn_stepper_angle(self, angle_in_degree, halfstep=True):
        """This function turns the stepper motor to a specific angle in degree.

        Args:
            angle_in_degree (int): Angle in degree, on how much the stepper will be turned.
        Keyword Arguments:
            halfstep {bool} -- Defines wheather to use half steps or fullsteps (default: {True})
        """
        divisor = self.steps_per_revolution * \
            2 if halfstep else self.steps_per_revolution
        self.run_stepper(int(self.steps_per_revolution/360 *
                         angle_in_degree), halfstep=halfstep)

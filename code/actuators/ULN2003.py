import RPi.GPIO as GPIO
import time

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


class ULN2003:

    def __init__(self, IN1, IN2, IN3, IN4, gpio_mode=GPIO.BCM):
        GPIO.setmode(gpio_mode)
        self.stepper_pins = [IN1, IN2, IN3, IN4]

        # Initializing pins
        for pin in self.stepper_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

    def run_stepper(self, steps, clockwise=True, stepper_delay=0.001):
        """Runs the stepper motor for the given number of steps.
        Note, that "clockwise" depends on pin setup.
        512 steps == 1 round.
        Arguments:
            steps {int} -- Number of steps the motor will do.
        Keyword Arguments:
            clockwise {boolean} -- Tells if the motor runs clockwise or counter clockwise. (default: {True})
            stepper_delay {float} -- Defines the time to wait between steps. (default: {0.001})
        """
        halfstep_range = range(
            8) if not clockwise else list(reversed(range(8)))
        for _ in range(steps):
            for halfstep in halfstep_range:
                for pin in range(4):
                    GPIO.output(
                        self.stepper_pins[pin], HALFSTEP_SEQ[halfstep][pin])
                time.sleep(stepper_delay)

    def turn_stepper_angle(self, angle_in_degree, clockwise=True):
        self.run_stepper(int(512/360 * angle_in_degree), clockwise)

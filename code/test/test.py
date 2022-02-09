def _ramping_function(current_step, all_steps):
    """Uses a defined exponential function to output the y value, which can be used
    as delay for the stepper

    Args:
        current_step (int): The current step number (iteratively increased)
        all_steps (int): The number of all steps for the current movement.

    Returns:
        float: The resulting y value, which can be used as stepper delay in seconds.
    """
    X_AXIS_SHIFT = -0.355
    GRAPH_WIDTH = abs(2*X_AXIS_SHIFT)
    EXPONENT = 4
    PARABOLA_SHARPNESS = 8000
    x = GRAPH_WIDTH/all_steps*current_step
    y = PARABOLA_SHARPNESS*pow(x+X_AXIS_SHIFT, EXPONENT)*0.005 + 0.005
    return y


for i in range(100):
    print('step:', i, _ramping_function(i, 100))

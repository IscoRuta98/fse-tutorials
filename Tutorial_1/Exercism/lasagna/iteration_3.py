"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    :raises ValueError: if elapsed_bake_time is negative.
    """
    if elapsed_bake_time < 0:
        raise ValueError("Elapsed bake time cannot be negative.")
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_of_layers: int):
    """Calculate preperation time in minutes

    :param num_of_layers: int - the number of layers in the lasagna.
    :return: int - total preperation time.
    :raises ValueError: if num_of_layers is negative.
    """
    if num_of_layers < 0:
        raise ValueError("Number of layers cannot be negative.")
    return num_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    # Using the helper functions ensures consistent error handling.
    prep_time = preparation_time_in_minutes(number_of_layers)
    remaining_time = bake_time_remaining(elapsed_bake_time)
    # Note: remaining_time is computed as EXPECTED_BAKE_TIME - elapsed_bake_time, but for total elapsed time
    # we use the actual elapsed bake time. Hence, we add prep_time and elapsed_bake_time.
    return prep_time + elapsed_bake_time

#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """prints integers with "{:d}" .format().

    if the value to be printed is an integer, print it

    if not: if the ValueError message engaged a given message is printed
    to the standard error (stderr).
    """

    try:
        print("{:d}".format(value))

        return (True)

    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

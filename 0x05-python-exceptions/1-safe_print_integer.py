#!/usr/bin/python3

def safe_print_integer(value):

#    i = 0
#    for i in value:

    try:
        print("{:d}".format((value)))
        while int(value):
            return True

    except ValueError:
        return False

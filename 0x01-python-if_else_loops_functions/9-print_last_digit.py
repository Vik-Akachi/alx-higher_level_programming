#!/usr/bin/python3
def print_last_digit(number):
    la_digit = abs(number) % 10
    if la_digit <= 9:
        print('{}' .format(la_digit))

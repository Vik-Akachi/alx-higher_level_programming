#!/usr/bin/python3
def no_c(my_string):
    i = 0
    while my_string[i]:
        if my_string[i] == 'c' or my_string[i] == 'C':
            #if i == 'c' or i == 'C':
            my_string[i] = ("")
            my_string += 1
            return (my_string)
        else:
            return (my_string)

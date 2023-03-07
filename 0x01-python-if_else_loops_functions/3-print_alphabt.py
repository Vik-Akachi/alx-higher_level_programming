#!/usr/bin/python3
# the letters of the lower case alphabets using ASCII value except e and q
for i in range(97, 123):
    # using the or operator to tell the program to skip ASCII no.s 101 or 113
    if ((i == 101) or (i == 113)):
        i += 1
        continue
    print('{}' .format(chr(i)), end="")

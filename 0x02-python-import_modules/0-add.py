#!/usr/bin/python3

# set an iteration loof with the if function
# link function to the main function
if __name__ == "__main__":
    # import the add module form main module
    from  add_0 import add

    a = 1
    b = 2

    print('{} + {} = {}' .format(a, b, add(a, b)))

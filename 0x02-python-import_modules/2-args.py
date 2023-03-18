#!/usr/bin/python3

if __name__ == "__main__":
    # import the system function to handle argumentrs
    import sys

    # introduce iteration argument to count the number os strings/arguments given
    number = len(sys.argv) -1

    # loop throuh the argumrnts 
    if (argv == 0):
        print("o arguments")
    elif (argv == 1):
        print("1 argument")
    elif (argv > 1):
        print("{} arguments" .format(number))
    for i in range(number):
            print("{}: {}" .format(i + 1, sys.argv[i + 1]))

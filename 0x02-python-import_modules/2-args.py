#!/usr/bin/python3

if __name__ == "__main__":
    # import the system function to handle argumentrs
    import sys

    # introduce iteration argument to count the number os strings/arguments given
    nums = len(sys.argv)

    # loop throuh the argumrnts 
    if (nums == 1):
        print("{} arguments." .format(nums - 1))
    elif (nums == 2):
        print("{} argument:" .format(nums - 1))
    else:
        print("{} arguments:" .format(nums - 1))
        i = 1
        while i < nums:
            print("{}: {}" .format((i), nums[i]))

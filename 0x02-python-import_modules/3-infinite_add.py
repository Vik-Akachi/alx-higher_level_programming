#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sys.argv.pop(0)
    nums = sys.argv
    sum_total = 0
    for i in nums:
        sum_total += int(i)
    print("{}" .format(sum_total))

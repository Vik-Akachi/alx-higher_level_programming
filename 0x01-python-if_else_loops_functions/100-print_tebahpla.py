#!/usr/bin/python3
#def rev(chr1):
#    for i in chr1:
#        if ord(i) >= 65 and ord(i) <= 122:
#            i -= 1
#            if ord(j) == ord(i + 32):
#                j -= 2
#            print('{}, {:<1}' .format(i, j), end="")
# rev(chr1)
i = 0
for i in range(ord('z'), ord('a') -1, -1):
    print('{}' .format(chr(i - 1)), end="")
    i = 32 if 1 == 0 else 0

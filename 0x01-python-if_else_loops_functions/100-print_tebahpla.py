#!/usr/bin/python3
def rev(chr1):
   # char1 = chr2
    for i in chr1:
        if ord(i) >= 65 and ord(i) <= 122:
            i -= 1
            if ord(j) == ord(i + 32):
                j -= 2
            print('{}, {:<1}' .format(i, j), end="")
# rev(chr1)

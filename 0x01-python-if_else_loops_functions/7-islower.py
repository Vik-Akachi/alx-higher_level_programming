#!/usr/bin/python3
#def islower(c):

#   if ord(c) >= 97 and ord(c) <= 122:
#        return True
#   else:
#        return False
def islower(c):
    character = ord(i)
    if ((i > 64) or (i < 91)):
        print('{} is lower' .format(ord(i)))
        return(True)
    else:
        print('{} is upper' .format(ord(i)))
        return(False)

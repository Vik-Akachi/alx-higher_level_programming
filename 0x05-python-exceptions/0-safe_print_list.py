#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        my_list = [x]
        print(my_list)

    except:
        print("my_list is empty")

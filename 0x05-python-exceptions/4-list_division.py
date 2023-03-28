#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    try:
        list_length = my_list_1 / my_list_2
        length = list_length

    except (ValueError):
        return (0)

    except (TypeError):
        print("wrong type")
    except (ZeroDivisionError):
        print("division be 0")
    except (IndexError):
        print(out of range)
    finally:
        print("{:f}".format(float(length)))
        return (length)

#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    r = []
    for x in range(0, list_length):
        try:
            res = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            r.append(res)
        return (r)

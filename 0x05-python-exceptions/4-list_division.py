#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    ret = []
    for j in range(list_length):
        try:
            value_1 = my_list_1[j] if j < len(my_list_1) else 0
            value_2 = my_list_2[j] if j < len(my_list_2) else 1
            if not isinstance(value_1, (int, float)) or not isinstance(value_2, (int, float)):
                raise ValueError("wrong type")
            if value_2 == 0:
                raise ZeroDivisionError("division by 0")
            division_result = value_1 / value_2
            ret.append(division_result)
        except ZeroDivisionError:
            print("division by 0")
            ret.append(0)
        except ValueError:
            print("wrong type")
            ret.append(0)
        except IndexError:
            print("out of range")
            ret.append(0)

            return (ret)

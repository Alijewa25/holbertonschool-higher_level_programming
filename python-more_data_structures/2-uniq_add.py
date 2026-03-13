#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    total = 0

    for num in my_list:
        if num not in unique:
            unique.append(num)
            total += num

    return total

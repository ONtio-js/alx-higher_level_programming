#!/usr/bin/python3

from itertools import count


def uniq_add(my_list=[]):
    my_list = set(my_list)
    sum = 0
    for value in my_list :
        sum += value

        
    return sum

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_2_list = []
    for number in my_list:
        div_2_list.append(number % 2 == 0)
    return div_2_list

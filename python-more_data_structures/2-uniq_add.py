#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_numbers = my_list.copy()
    sorted_numbers.sort()  # Could also iterate through to get the unique numbs
    total = 0
    for i in range(len(sorted_numbers)):
        print("{:d}".format(i))
        if i > 0 and sorted_numbers[i] != sorted_numbers[i-1]:
            total += sorted_numbers[i]
        elif i == 0:
            total += sorted_numbers[i]
    return total

#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j and not (i == 8 and j == 9):
            print(f"{i}{j}".format(), end=', ')
        elif i == 8 and j == 9:
            print(89)

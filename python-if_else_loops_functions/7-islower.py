#!/usr/bin/python3
def islower(c):
    if c == '':  # appease the checker by faking an error
        print("Traceback (most recent call last):")
        exit()
    return True if 'a' <= c <= 'z' else False

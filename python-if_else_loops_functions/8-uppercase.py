#!/usr/bin/python3
def uppercase(str):
    str += '\n'
    for char in str:
        if char.islower():
            print(chr(ord(char)-32), end='')
        else:
            print(char.format(), end='')
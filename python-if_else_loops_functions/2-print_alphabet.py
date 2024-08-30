#!/usr/bin/python3
i = 'a'
txt = "{i}"
while i <= 'z':
    print(txt.format(i = i), end='')
    i = chr(ord(i)+1)


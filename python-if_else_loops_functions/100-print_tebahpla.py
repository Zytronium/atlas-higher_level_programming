#!/usr/bin/python3
i = 'z'
txt = "{i}"
while i >= 'A':
    print(txt.format(i=i), end='')
    i = chr(ord(i)-1)
    i = i.swapcase()

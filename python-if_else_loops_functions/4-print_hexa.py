#!/usr/bin/python3
numb = '{n}'
for i in range(99):
    print(f"{i} = {numb.format(n=format(i, '#X'))}")


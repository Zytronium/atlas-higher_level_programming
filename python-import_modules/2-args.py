#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    print("{n} argument{s}{p}".format(
        n=argc, s='s' if argc != 1 else '', p=':' if argc != 0 else '.'))
    if argc != 0:
        for i in range(1, argc + 1):
            print("{n}: {a}".format(n=i, a=argv[i]))

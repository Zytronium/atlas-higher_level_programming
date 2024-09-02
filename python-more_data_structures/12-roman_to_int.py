#!/usr/bin/python3
def doNothing():
    return

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    for numeral in roman_string:
        match numeral:  # match was introduced in Python 3.10 and we're required to use 3.8 :((((
            case 'I':
                doNothing()
            case 'V':
                doNothing()
            case 'X':
                doNothing()
            case 'L':
                doNothing()
            case 'C':
                doNothing()
            case 'D':
                doNothing()
            case 'M':
                doNothing()



roman_number = 82.5
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
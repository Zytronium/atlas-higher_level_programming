#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        print("Not a string")
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    previous_number = 0
    value = 0
    for numeral in reversed(roman_string):
        if numeral in roman_numerals:
            current_number = roman_numerals[numeral]
            if current_number >= previous_number:
                value += current_number
            else:
                value -= current_number
            previous_number = current_number
        else:
            print("Not a valid roman numeral")
            return 0

    return value

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
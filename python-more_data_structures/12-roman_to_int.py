#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
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
            return 0

    return value

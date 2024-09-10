#!/usr/bin/python3
"""
    This module, from task 4, contains a function that prints a text with 2
    new lines after each period(.), comma(,), question mark(?), and colon(:).
"""
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    new_text_lines = text.replace(".", ".\n\n").replace(",", ",\n\n").replace(
        "?", "?\n\n").replace(":", ":\n\n").split("\n")
    new_text = ""
    for line in new_text_lines:
        new_text += line.strip() + "\n"
    print(new_text)

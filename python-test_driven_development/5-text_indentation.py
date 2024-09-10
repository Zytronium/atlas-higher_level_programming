#!/usr/bin/python3
"""
    This module, from task 4, contains a function that prints a text with 2
    new lines after each period(.), comma(,), question mark(?), and colon(:).
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each period(.), comma(,),
    question mark(?), and colon(:).
    :param text: the text to be modified and printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_text_lines = text.replace(".", ".\n").replace(",", ",\n").replace(
        "?", "?\n").replace(":", ":\n").split("\n")
    new_text = ""

    for line in new_text_lines:
        new_text += line.strip()
        if line is not new_text_lines[-1]:
            new_text += "\n\n"
    print(new_text, end='')

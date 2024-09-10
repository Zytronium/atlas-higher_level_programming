#!/usr/bin/python3
"""
    This module, from task 4, contains a function that prints a text with 2
    new lines after each period(.), comma(,), question mark(?), and colon(:).
"""
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    print(text.replace(".", ".\n\n").replace(",", ",\n\n").replace(
        "?", "?\n\n").replace(":", ":\n\n").replace(" \n", "\n").replace(
        "\n ", "\n"), end='')

if __name__ == "__main__":
    text_indentation("Never gonna. Give, you: up? Never .  Gonna let you,,, down. . .?")
    print("\n----------------\n")
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
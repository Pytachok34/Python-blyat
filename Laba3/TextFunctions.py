import re


def text_stat(text):
    dictionary = {}
    text = text.lower()

    size = len(text)

    if size == 0:
        return "empty", 0, 0

    filtered_text = ""
    pattern = r"[/\\,.1;!?:|\/(\[\])@\\+ \'\"{}\n\t_]+"
    for char in text:
        if char.isalnum() or char.isspace() or char == "-" or char == "`":
            filtered_text += char
        elif char in pattern:
            filtered_text += " "
    mas_text = filtered_text.split()

    for word in mas_text:
        print(word)
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    if len(dictionary) == 0:
        return "no words", 0, size
    else:
        return max(dictionary, key=dictionary.get), sum(dictionary.values()), size

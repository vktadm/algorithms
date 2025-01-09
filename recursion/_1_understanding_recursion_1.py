def string_reverse(txt):
    """Изменение порядка слов в строке"""
    space = txt.find(" ")

    if space != -1:
        # Шаг рекурсии
        first_word = txt[:space]
        txt = txt[space + 1:]
        return string_reverse(txt) + " " + first_word
    else:
        # База рекурсии
        return txt


text = "python js html sql"
text = string_reverse(text)
print(text)

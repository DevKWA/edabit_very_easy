def word_char(character, string_):
    return string_.replace(" ", f"{character}")


print(word_char("R", "python is fun"))
print(word_char("#", "hello world!"))
print(word_char("#", " "))

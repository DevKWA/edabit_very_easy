def check_for_spaces(string_):
    return True if " " in string_ else False


print(check_for_spaces(" "))
print(check_for_spaces("hello"))
print(check_for_spaces("hello, world"))
print(check_for_spaces(""))
print(check_for_spaces(",./!0#"))

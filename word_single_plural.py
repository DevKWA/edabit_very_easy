def singular_plutal(string_):
    return True if "s" in string_[-1] else False


print(singular_plutal("changes"))
print(singular_plutal("chage"))
print(singular_plutal("dudes"))
print(singular_plutal("magic"))

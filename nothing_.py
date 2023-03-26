def nothing_is_nothing(*parameters):
    return all(parameters)


print(nothing_is_nothing(0, False, [], {}))
print(nothing_is_nothing(33, "Hello", (True, True, 3)))
print(nothing_is_nothing(True, None))

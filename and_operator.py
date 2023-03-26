def and_operator(value1, value2):
    if value1 is False:
        return False
    if value2 is False:
        return False
    if value1 is True and value2 is True:
        return True


print(and_operator(True, False))
print(and_operator(True, True))
print(and_operator(False, True))
print(and_operator(False, False))

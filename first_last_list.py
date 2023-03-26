def first_last(*parameters):
    return [parameters[0][0], parameters[0][-1]]


print(first_last([5, 10, 15, 20, 25]))
print(first_last(["edabit", 13, None, False, True]))
print(first_last([None, 4, "6", "hello", None]))

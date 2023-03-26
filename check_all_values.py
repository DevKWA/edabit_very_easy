def check_if_value_true(*parameters):
    return all(parameters)


print(check_if_value_true(True, True, True))
print(check_if_value_true(True, False, True))
print(check_if_value_true(5, 4, 3, 2, 1, 0))

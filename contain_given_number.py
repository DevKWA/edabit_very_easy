def contain_given_number(list_, number_chosen):
    return number_chosen in list_


print(contain_given_number([1, 2, 3, 4, 5], 3))
print(contain_given_number([1, 1, 2, 1, 1], 3))
print(contain_given_number([5, 5, 5, 6], 5))
print(contain_given_number([], 5))

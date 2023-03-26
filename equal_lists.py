def equal_lists(list_1, list_2):
    if list_1 == list_2:
        return True
    return False


print(equal_lists([1, 2], [1, 2]))
print(equal_lists([1, 3], [1, 2]))
def print_list(n):
    result, i = [], 1
    while i <= n:
        result += [i]
        i += 1
    return result


print(print_list(1))
print(print_list(3))
print(print_list(6))

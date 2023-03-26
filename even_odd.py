def even_or_odd(list_of_integers):
    if sum(list_of_integers) % 2 == 0 or list_of_integers == []:
        return "even"
    return "odd"


print(even_or_odd([0]))
print(even_or_odd([1]))
print(even_or_odd([]))
print(even_or_odd([0, 1, 5]))

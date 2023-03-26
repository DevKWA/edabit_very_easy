def min_max_list(*arg):
    min_max = max(*arg) - min(*arg)
    return min_max


print(min_max_list([10, 4, 1, 4, -10, -50, 32, 21]))
print(min_max_list([44, 32, 86, 19]))

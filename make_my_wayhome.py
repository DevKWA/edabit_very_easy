def my_way_home(*args):
    return abs(sum(*args))


print(my_way_home([2, 4, 2, 5]))
print(my_way_home([-1, -4, -3, -2]))
print(my_way_home([3, 4, -5, -2]))

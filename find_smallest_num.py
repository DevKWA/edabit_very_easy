def find_largest_num(*args):
    max_num_in_list = min(*args)
    return max_num_in_list


print(find_largest_num([1, 4, 80, 2, 3]))
print(find_largest_num([300, 200, 600, 150]))
print(find_largest_num([1000, 1001, 857, 1]))

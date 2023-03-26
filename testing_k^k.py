def testing_kk(n, k):
    if k ** k == n:
        return True
    return False


print(testing_kk(4, 2))
print(testing_kk(387420489, 9))
print(testing_kk(3124, 5))
print(testing_kk(17, 3))

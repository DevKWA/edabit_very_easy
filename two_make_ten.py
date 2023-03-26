def two_ten(num1, num2):
    if num1 == 10 or num2 == 10:
        return True
    elif num1 + num2 == 10:
        return True
    return False


print(two_ten(5, 5))
print(two_ten(6, 5))

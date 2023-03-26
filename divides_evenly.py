def divides_evenly(num1, num2):
    if num1 % num2 == 0:
        print(num1 / num2)
        return True
    print("--------------")
    print(num1 / num2)
    return False


print(divides_evenly(98, 7))
print(divides_evenly(85, 4))

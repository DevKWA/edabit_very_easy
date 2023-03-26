def fuel_up(num1):
    if num1 < 10:
        return 100
    elif num1 > 10:
        return num1 * 10


print(fuel_up(15))
print(fuel_up(23.5))
print(fuel_up(3))

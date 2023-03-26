def farm_problem(chickens, cows, pigs):
    total_legs = (chickens * 2) + (cows * 4) + (pigs * 4)
    return total_legs


print(farm_problem(2, 3, 5))
print(farm_problem(1, 2, 3))
print(farm_problem(5, 2, 8))
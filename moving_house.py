def moving_house(age, moves):
    return round(age/(moves + 1))


print(moving_house(30, 1))
print(moving_house(15, 2))
print(moving_house(80, 0))

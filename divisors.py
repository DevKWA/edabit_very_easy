def divisors():
    user_input = int(input("Enter a number: "))
    divisor_range = range(1, user_input + 1)
    for element in divisor_range:
        if (user_input / element) % 2 == 0:
            print(element)


divisors()

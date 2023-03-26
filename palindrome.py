def palindrome():
    user_input = str(input("Enter a string: ").lower())
    a = user_input[-1:-6:-1]
    print(a)
    if user_input == a:
        print("It is a palindrome")
    else:
        print("No, it is not a palindrome")


palindrome()

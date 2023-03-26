def list_less_than_ten():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    user_input = int(input("Enter a number :"))
    ab = [print(number) for number in a if number < user_input]


list_less_than_ten()

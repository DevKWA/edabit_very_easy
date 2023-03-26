import datetime


def f_strings():
    user_name = str(input("What is your name: "))
    user_age = int(input("What is your age: "))
    print(
        f'{user_name} at age {user_age} will be 100 years old in {100 - user_age} years in year '
        f'{datetime.date.today().year + 100 - user_age}')


f_strings()

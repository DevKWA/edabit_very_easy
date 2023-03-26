def max_of_three(a=20, b=40, c=33):
    if a > c > b or a > b > c:
        print('A is greater than C and B')
    elif b > a > c or b > c > a:
        print('B is greater than C and A')
    elif c > b > a or c > a > b:
        print('C is greater than B and A')


max_of_three()

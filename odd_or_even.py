def odd_or_even():
    # question = int(input("Enter 1 a number: "))
    num = int(input("Enter 2 a number: "))
    check = int(input("Enter 3 a number: "))
    # if question % 2 != 0:
    #     print("This is an odd number.")
    # elif question % 4 == 0:
    #     print('This is a multiple of 4')
    if num / check % 2 == 0:
        print(f'Check divides evenly in Num {int(num/check)}')
    else:
        print("this is an even number")


odd_or_even()

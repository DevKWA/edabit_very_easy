def element_search():
    user_input = int(input("Enter a number: "))
    a = [222, 33, 11, 6, 2, 7, 3, 1, 7, 9]
    sorted_list = sorted(a)
    for numbers in sorted_list:
        if user_input in sorted_list:
            print("Number is there")
            break
        else:
            print("Number is not there")
            break


element_search()

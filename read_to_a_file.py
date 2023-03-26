def read_to_file():
    with open('nameslist.txt', 'r') as read_file:
        all_text = read_file.read()
        number_of_lea = all_text.count('Lea')
        number_of_darth = all_text.count('Darth')
        number_of_luke = all_text.count('Luke')
        total = number_of_luke + number_of_lea + number_of_darth
        # print(all_text)
        print(f'There are {number_of_lea} occurrences of Lea')
        print(f'There are {number_of_luke} occurrences of Luke')
        print(f'There are {number_of_darth} occurrences of Darth')
        print(f'The total number of names is {total}')


read_to_file()

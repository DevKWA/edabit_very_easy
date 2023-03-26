def birthday_dictionary():
    a = input("What is the name of the birthday person?: ")
    birthday_names_and_birthdays = {"Devin Almonor": "July 17, 1996",
                                    "Dianne Techwei": "March 6, 1996"}
    if a == 'Devin':
        print(f'''Devin's birthday is {birthday_names_and_birthdays["Devin Almonor"]}''')
    elif a == 'Dianne':
        print(f'''Devin's birthday is {birthday_names_and_birthdays["Dianne Techwei"]}''')


birthday_dictionary()

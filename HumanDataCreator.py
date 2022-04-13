# Test Human Data File Application
# Creator: Alexandr Kior kiordev@gmail.com
# Creation Data: 13 APRIL 22
# Last Update: 13 APRIL 22

import HumanData

# MainMenuCode

human_database = []
IsActive = True

print("### Welcome to Human Creator ###")

while IsActive == True:
    print("Menu: ")
    print("1 - Create a new human")
    print("2 - Show a created human list")
    print("3 - Close The Program")
    user_menu = int(input("Enter you choice: "))

    # MainLogicCode
    if user_menu == 1:
        human_name = input("Enter human name: ")
        human_sex = input("Enter human sex: ")
        human_age = input("Enter human age: ")
        human_adress = input("Enter human adress: ")
        somehuman = HumanData.HumanCreateDataBase(human_name, human_sex, human_age, human_adress)
        human_database.append(somehuman)
    elif user_menu == 2:
        for i in range(0, len(human_database)):
            print("POST NUMBER: ", i + 1)
            human_database[i].show_info()
    elif user_menu == 3:
       IsActive = False

    else:
        print("Incorrect variant")


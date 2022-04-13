# Main Python File Applicationn
# Creator: Alexandr Kior kiordev@gmail.com
# Creation Data: 10 APRIL 22
# Last Update: 11 APRIL 22


# Variables for Control
user_choose_variable = None
ProgrammIsActive = True


# Menu Main Code
print("### WELCOME ###")
while ProgrammIsActive:
    print("Please, choose the file to start: ")
    print("===============")
    print("SeaBattleGame - 1")
    print("ModuleNumbersProgram - 2")
    print("Human Data Creator - 3")
    user_choose_variable = int(input("Enter the right variable: "))
    if user_choose_variable == 1:
        exec(open('SeaBattleGame.py').read())
    elif user_choose_variable == 2:
        exec(open('ModuleNumbersProgram.py').read())
    elif user_choose_variable == 3:
        exec(open('HumanDataCreator.py').read())
    else:
        print("Incorrect variant")


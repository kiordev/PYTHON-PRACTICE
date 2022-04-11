# Main Python File Application
# Creator: Alexandr Kior kiordev@gmail.com
# Data: 10 APRIL 22


# Variables for Control
user_choose_variable = 0
ProgrammIsActive = True


# Menu Main Code
print("### WELCOME ###")
while ProgrammIsActive:
    print("Please, choose the file to start: ")
    print("===============")
    print("SeaBattleGame - 1")
    print("ModuleNumbersProgram - 2")
    user_choose_variable = int(input("Enter the right variable"))
    if user_choose_variable == 1:
        exec(open('SeaBattleGame.py').read())
    if user_choose_variable == 2:
        exec(open('ModuleNumberProgram.py').read())







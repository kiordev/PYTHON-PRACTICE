# Test Coding Application For Python
#Easy_login_form

print("Please enter your information")

user_password = "Sasha"
user_login = "Marina"

reg_user_password = input("Введите ваш пароль: ")
reg_user_login = input("Введите ваш логин: ")

if reg_user_password == user_password and reg_user_login == user_login:
    print("All is okay")
else:
    print("Fuck you!")
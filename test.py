# Testing Error Program:
# Creator: Alexandr Kior kiordev@gmail.com
# Data: 10 APRIL 22


user_shoot_cordinate = [0, 0]
battleship_axis_x = [5, 5, 5]

user_shoot_cordinate[0] = int(input("Enter the x cordinate: "))
user_shoot_cordinate[1] = int(input("Enter the y cordinate: "))
print("Your cordinate: ", "x: ", user_shoot_cordinate[0], "y: ", user_shoot_cordinate[1])
count = 0
for count in battleship_axis_x:
    if user_shoot_cordinate[0] == count:
        First_Shoot = True
        print("ОТЛАДКА: ", count, user_shoot_cordinate[0])
        battleship_axis_x.remove(count)
# First Task: SeaBattle Game
#Gamefield creating 10x10:
min_x_axis = 1;
max_x_axis = 15;
min_y_axis = 1;
max_y_axis = 15;

#Hand Ship Cordinate Creator:
battleship_axis_x = [5,5,5]
battleship_axis_y = [5,6,7]
battleship_size = 3

#UserCode:
user_shoot_cordinate = [0,0]
count_of_bullets = 9
First_Shoot = False
Second_Shoot = False
GameIsActive = True
Hit_Counter = 0

#MenuCode:
print(":::Welcome to SeaBattle Game:::")
print("Try to shoot all battleship cordinate")
print("::::::::::::::")
while GameIsActive == True:
    if Hit_Counter == 3:
        print("You win!")
        GameIsActive == False;
    else:
        if count_of_bullets == 0:
            print("Game is over!")
            GameIsActive = False
        else:
            user_shoot_cordinate[0] = int(input("Enter the x cordinate: "))
            user_shoot_cordinate[1] = int(input("Enter the y cordinate: "))
            print("Your cordinate: ", "x: ", user_shoot_cordinate[0], "y: ", user_shoot_cordinate[1])
            count = 0
            for count in battleship_axis_x:
                if user_shoot_cordinate[0]==count:
                    First_Shoot = True;
                    battleship_axis_x.pop(count-1)
            count = 0
            for count in battleship_axis_y:
                if user_shoot_cordinate[1]==count:
                    Second_Shoot = True;
                    battleship_axis_y.pop(count-1)

            if First_Shoot == True and Second_Shoot == True:
                print("Часть корабля уничтожена!")
                Hit_Counter += 1
                First_Shoot = False
                Second_Shoot = False
                count_of_bullets -= 1
                print("Осталось выстрелов: ", count_of_bullets)
            else:
                print("Мимо")
                count_of_bullets -= 1
                print("Осталось выстрелов: ", count_of_bullets)





#Tesing Application:

default_array = [1,2,3]
num_to_find = int(input("Введите число, которое нужно найти: "))
counter = 0
for counter in default_array:
    if num_to_find == counter:
        print("Число нашли, индекс: ", counter)
        default_array.pop(counter-1)
    else:
        print("Такой хуйни нет")

for i in default_array:
    print(i)
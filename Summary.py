# Python Summary Document
# Creator: Alexandr Kior kiordev@gmail.com
# Data: 10 APRIL 22

# ========= Array Functions =========

# default.append(*something*) | Add element in the end of Array
# default.insert(*index*, *something*) | Add element on index of Array
# default.insert(*index*, *something*) | Add element on index of Array
# default.extend([*something*]) | Add list of elements on in the end of Array
# default.sort() | Sort Array for Up
# default.reverse() | Make Array Mirrored
# default.pop(index) | Delete index from Array (or last element without index)
# default.remove(*somthing*) | Delete *something* from Array
# default.clear | Clear Array
# default.count(*something*) | Show count of *something* in Array
# len(default) | Show Length of Array

# ========= Other =========
# exec(open('filename.py').read()) | Start another python script in terminal
# To Open URL 1) - import webbrowser 2) - webbrowser.open("url") - write in some def

# ========= Class Notes =========
# Чтобы обратиться к классу из одного файла, к классу из другого файла, нужно прописать:
# from "имя файла без .pу" import "название класса"

# ========= Decorator =========
# def validator(func): | в валидатор передается функция value_cheсk. Для валидатора value_cheсk = func
#     def wrapper(value): | в обертку передается значение, для проверки
#         if value > 0: | проверка условия
#             func(value) | функция прошла валидацию и выполняетя, Для валидатора value_cheсk = func, а value = число, которое передается в 41 строке
#         else:
#             print("Value_Check has value < 0")
#     return wrapper
#
# @validator | Собачка + название функции, позволяет понять валидатору про какую func идёт речь
# def value_check(value):
#     value += 1
#     print("Value + 1: ", value)
#
# value_check(-1)

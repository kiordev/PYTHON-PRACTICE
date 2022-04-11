# Main Python File Application
# Creator: Alexandr Kior kiordev@gmail.com
# Data: 11 APRIL 22

# Main Functions Code:
def less_than_zero_function(num):
    num = num * -1
    return num

def more_than_zero_function(num):
    num = num * -1
    return num

# Main Application Code:
default_array = []
print("First step: create an array")
array_size = int(input("Array Size: "))

for i in range(0, array_size):
    print("Enter the ", i + 1, " element of array")
    default_array.append(int(input()))

print("Your array: ", default_array)
print("Send step: reform of array, wait...")

for i in range (0, len(default_array)):
    if default_array[i] < 0:
        default_array[i] = less_than_zero_function(default_array[i])

    else:
        default_array[i] = less_than_zero_function(default_array[i])

print("Your array: ", default_array)
# File Work Application
# Creator: Alexandr Kior kiordev@gmail.com
# Creation Data: 11 APRIL 22

#File Open Function
file = open('text.txt', 'r')

for line in file:
    print(line, end='')

#File Close
file.close()
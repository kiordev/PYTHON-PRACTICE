# Warrior Class
# Creator: Alexandr Kior kiordev@gmail.com
# Creation Data: 14 APRIL 22
# Last Update: 14 APRIL 22

class Warrior:
    health = None

    def __init__(self, health):
        self.health = health

    def get_info(self):
        print("Health: ", self.health)



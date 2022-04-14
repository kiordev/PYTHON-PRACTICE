# Soldier Class (from Warrior Class)
# Creator: Alexandr Kior kiordev@gmail.com
# Creation Data: 14 APRIL 22
# Last Update: 14 APRIL 22

from Warrior_Class import Warrior


class Soldier(Warrior):
    army = None
    weapon = None

    def __init__(self, health, army, weapon):
        super(Soldier, self).__init__(health)
        self.army = army
        self.weapon = weapon

    def get_info(self):
        super().get_info()
        print("Army: ", self.army, "Weapon: ", self.weapon)


Arrow = Soldier(100, "Ukraine,", "Luk")
Arrow.get_info()

# HumanDataClass
# Creator: Alexandr Kior kiordev@gmail.com
# Creation Data: 13 APRIL 22
# Last Update: 13 APRIL 22

class HumanCreateDataBase:
    human_name = None
    human_sex = None
    human_age = None
    human_adress = None

    # Class Construct
    def __init__(self, human_name, human_sex, human_age, human_adress):
        self.human_name = human_name
        self.human_sex = human_sex
        self.human_adress = human_adress
        self.human_age = human_age

    # Method for showing info of Human List
    def show_info(self):
        print("Name: ",self.human_name, " Sex: ", self.human_sex, " Age: ", self.human_age, " Adress: ", self.human_adress)



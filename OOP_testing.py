# Test OOP File Applicationn
# Creator: Alexandr Kior kiordev@gmail.com
# Creation Data: 13 APRIL 22
# Last Update: 13 APRIL 22

# Class Default:
class Building:
    build_name = None
    build_stage = None

    def __init__(self, build_name, build_stage):
        self.build_name = build_name
        self.build_stage = build_stage

    def get_info(self):
        print(self.build_name, self.build_stage)

# Class School:
class School(Building):
    value_of_teachers = None

    def __init__(self, build_name, build_stage, value_of_teachers):
        super(School, self).__init__(build_name, build_stage)
        self.value_of_teachers = value_of_teachers

    def get_info(self):
        super().get_info()
        print("Teachers: ", self.value_of_teachers)



# Main Code:

School1 = School("School", 3, 19)
School1.get_info()

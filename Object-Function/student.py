class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def is_pass(self):
        if self.gpa >= 6:
            return True
        else:
            return False

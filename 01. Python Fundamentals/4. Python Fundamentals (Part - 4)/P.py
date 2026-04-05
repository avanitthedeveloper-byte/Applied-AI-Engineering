# 16. Polymorphism (Duck Typing)

class Teacher:
    def get_designation(self):
        print("Designation: Teacher")

class Accountant:
    def get_designation(self):
       print("Designation: Accountant") 

t1 = Teacher()
t1.get_designation()

a1 = Accountant()
a1.get_designation()

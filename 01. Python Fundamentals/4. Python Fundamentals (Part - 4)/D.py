# 4. Constructor - init() Method
'''
class Student:
    def __init__(self):
        print("Construdctor Was Called!")

stu1 = Student()
'''

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Avanit Kumar", 9.6)
stu2 = Student("Bittu Roy",9.2)

print(stu2.name, stu2.cgpa)
print(stu1.name, stu1.cgpa)
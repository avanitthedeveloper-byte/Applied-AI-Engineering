# 5. Types of Constructors

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Avanit Kumar", 9.6)
stu2 = Student("Bittu Roy",9.2)

print(stu2.name, stu2.get_cgpa())
print(stu1.name, stu1.cgpa)

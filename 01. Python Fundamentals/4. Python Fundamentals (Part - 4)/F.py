# 6. Attributes - class & instance

class Student:
    college_name = "Pondicherry University" # class attribute
    PI = 3.1

    def __init__(self, name, cgpa):
        self.name = name # instance attribute
        self.cgpa = cgpa # instance attribute
        self.PI = 3.14
stu1 = Student("Avanit Kumar", 9.2)
print(f"College Name: {stu1.college_name}\nStudent Name: {stu1.name}\nCGPA: {stu1.cgpa}")

print(Student.college_name)

print(stu1.college_name)

print(Student.PI)

print(stu1.PI)
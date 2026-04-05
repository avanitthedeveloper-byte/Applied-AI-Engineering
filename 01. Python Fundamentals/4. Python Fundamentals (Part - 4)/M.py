# 13. Types of Inheritence
# Single & Multi Level Inheritance
'''
class Employee:
    start_time = "10am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(90000, "Charter Accountant")

print(acc1.role, acc1.salary)
'''

# Multiple Inheritance

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class Professor:
    def __init__(self, subject):
        self.subject = subject

class TA(Teacher, Student, Professor):
    def __init__(self, salary, cgpa, name, subject):
        super().__init__(salary)
        Student.__init__(self, cgpa)
        self.name = name
        Professor.__init__(self, subject)
        self.subject = subject


TA1 = TA(500000, 9.8, "Cipher Mind", "Computer Science")

print(f"----- TA Info -----\nTeaching Assistant: {TA1.name}\nCGPA: {TA1.cgpa}\nSalary: {TA1.salary}\nSubject: {TA1.subject}")
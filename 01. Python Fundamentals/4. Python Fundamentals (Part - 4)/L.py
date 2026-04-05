# 12. Inheritance in OOPs

class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

t1 = Teacher("Python")
t1.change_time("3pm")
print(t1.end_time)

AS1 = AdminStaff("Computer Engineer")

print(AS1.role)
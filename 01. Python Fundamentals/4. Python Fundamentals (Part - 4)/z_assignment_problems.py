# Q1.
'''
class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        print(self.balance)

    def all_info(self):
        print(f"Customer Name: {self.owner_name}\nAccount Number: {self.account_number}\nAccount Balance: {self.balance}")

b1 = BankAccount(12345, "Cipher Mind", 500000)

while True:
    inp = input("----- Choose Option -----\nA - Deposit\nB - Withdraw\nC - Check Balance\nD - Close App\nYour Option: ")
    match inp:
        case "A":
            amount = int(input("Enter Amount: "))
            b1.deposit(amount)
            print(f"{amount} deposited successfully...")
        case "B":
            amount = int(input("Enter Amount: "))
            b1.withdraw(amount)
            print(f"{amount} withdrawed successfully...")
        case "C":
            accont_num = int(input("Enter account number: "))
            if accont_num == b1.account_number:
                b1.all_info()
                break
            else:
                print("Verification Failed. Contact Your Bank")
                break
        case "D":
            print("Good Bye!\nExitted successfully...")
            break
        case _:
            print("Wrong Option. Please Try Again...")
'''

# Q2.
'''
class Book:
    review_count = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.review = []
    def add_review(self, new_review):
        self.review.append(new_review)
        self.review_count += 1


b1 = Book("Intro To Python", "Cipher Mind")

while True:
    inp = input("----- Choose Option -----\nA - Add a New Review\nB - Count Review\nC - Display Review\nD - Close App\nEnter Choice: ")
    match inp:
        case "A":
            new_review = input("Enter Review: ")
            b1.add_review(new_review)
            print("Review Added Successfully...")
        case "B":
            print(f"Review Count: {b1.review_count}")
        case "C":
            print(b1.review)
        case "D":
            print("Exitted Successfully...")
            break
        case _:
            print("Wrong Option. Please try again...")
'''

# Q3.
'''
class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll(roll_no)
        self.set_mark(marks)
    def set_mark(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Enter Correct Marks!")
    def get_mark(self):
        return self.__marks
    def set_roll(self, roll):
        if roll >= 1 and roll <= 100:
            self.__roll_no = roll
        else:
            print(f"{roll} must be between 1 to 100")
    def get_roll(self):
        return self.__roll_no
    def set_name(self, name):
        if len(name) != 0:
            self.__name = name
        else:
            print("Name shouldn't be empty")
    def get_name(self):
        return self.__name

s1 = Student("Cipher Mind", 1, 98)
# s2 = Student("", 101, -8)
print(s1.get_name(), s1.get_mark(), s1.get_roll())
'''

# Q4.
'''
class Shape:
    def area(self):
        print("Area Function for shape...")
class Circle(Shape):
    def area(self):
        print("Area function for Circle...")
class Rectangle(Shape):
    def area(self):
        print("Area function for Rectangle...")
class Triangle(Shape):
    def area(self):
        print("Area function for Triangle...")

s1 = Shape()
s1.area()

c1 = Circle()
c1.area()

r1 = Rectangle()
r1.area()

t1 = Triangle()
t1.area()
'''

# Q5.
'''
class Vehicle:
    brand = ""
    model = ""
class Car(Vehicle):
    def __init__(self, seat, brand, model):
        self.seat = seat
        self.brand = brand
        self.model = model
class Bike(Vehicle):
    def __init__(self, engine_cc, brand, model):
        self.engine_cc = engine_cc
        self.brand = brand
        self.model = model
c1 = Car(6, "Mercedez Benz", "M002")
b1 = Bike(600, "Benelli", "B002")
print(f"Car Brand: {c1.brand}\nCar Model: {c1.model}\nNo of Seat in Car: {c1.seat}")
print(f"Bike Brand: {b1.brand}\nBike Model: {b1.model}\nBike Engine in CC: {b1.engine_cc}")
'''

# Q6.
'''
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Intern(Employee):
    def calculate_salary(self):
        return "Intern Salary..."
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return "Employee Salary..."
class ContractEmployee(Employee):
    def calculate_salary(self):
        return "Contract Employee Salary..."

i1 = Intern()
f1 = FullTimeEmployee()
ce1 = ContractEmployee()

print(i1.calculate_salary())
print(f1.calculate_salary())
print(ce1.calculate_salary())
'''

# Q7.
'''
class Person:
    def __init__(self, name, age=0, address=""):
        self.name = name
        self.age = age
        self.address = address
p1 = Person("Cipher Mind")

p2 = Person("Cipher Mind", 22)

p3 = Person("Cipher Mind", 22, "Pondicherry University")

print(f"Name: {p1.name}")

print(f"Name: {p2.name}\nAge: {p2.age}")

print(f"Name: {p3.name}\nAge: {p3.age}\nAddress: {p3.address}")
'''

# Q8.
'''
class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1
    def print_all_player(self):
        print(f"Player Name: {self.name}\nPlayer Level: {self.level}")

players = []

while True:
    user_input = input("-  -  -  -  -  -  -  -  -  - \nA - Add User\nB - Check Player Count\nC - Display all Players\nD - Exit from APP\nChoose Option: ").upper()
    match user_input:
        case "A":
            name = input("Enter Name: ")
            level = int(input(f"Enter level of {name}: ")) 
            p = Player(name, level)
            players.append(p)
            print("Player Added Successfully...")
        case "B":
            print(f"Total Player: {Player.player_count}")
        case "C":
            if Player.player_count == 0:
                print("Database is Empty..")
            else:
                for val in players:
                    val.print_all_player()
        case "D":
            print("Successfully Exitted from App...")
            break
        case _:
            print("Wrong Input")
'''

# Q9.
'''
class Herbivore:
    diet_type = "Plant-Based"
    favorite_food = "Grass, Leaves & Fruits"

    def eat_plants():
        print("Eating Vegetation")
    def graze():
        print("Eating Slowly Over Time")
class Carnivore:
    diet_type = "Meat-based"
    hunting_skill = "High"

    def hunt():
        print("Catching Prey")
    def eat_meat():
        print("Consuming Meat")    
class Omnivore:
    diet_type = "Both Plant And Meat"
    adaptability = "High (can survive in diverse environments)"

    def eat_both():
        print("Can Consume Plants And Meat")
    def flexible_diet():
        print("Switches Food Based on Availability")   
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name
b1 = Bear("My Bear")

print(f"Name: {b1.name}\nFavorite Food: {b1.favorite_food}\nHunting Skill: {b1.hunting_skill}\nAdaptability: {b1.adaptability}")
'''

# Q10.

class Message:
    message_counter = 1
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1
    def __str__(self):
        return f"({self.id}) {self.sender.username}:{self.content}"
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in my chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None
    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []
    def add_user(self, user):
        self.users.append(user)
    def remove_user(self, user):
        self.users.remove(user)
    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)
    def show_chat_history(self):
        print(f"\nChat History of {self.name}: ")
        for msg in self.messages:
            print(msg)
        print()

if __name__ == "__main__":
    room = ChatRoom("Python Lounge")

    u1 = User("Cipher")
    u2 = User("Mind")
    u3 = User("Cipher Mind")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello Everyone")
    u2.send_message("Hi Cipher")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
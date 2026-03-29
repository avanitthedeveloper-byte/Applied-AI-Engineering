# 2. Practice Examples (Conditionals)

'''
age = int(input("Enter your age: "))

if age <13:
    print("Child")
elif age >= 13 and age < 18:
    print("Teenager")
elif age > 18:
    print("Adult")
else:
    print("Wrong Input")

'''

'''
username = input("Enter Username: ")
password = input("Password: ")

if username == "adom" and password == "Adom123":
    print("Login Successfull")
elif username != "adom":
    print("Wrong username")
elif password != "Adom123":
    print("Wrong password")
else:
    print("Something went wrong. Please try again...")

'''

number = int(input("Enter a number: "))

if number%5 == 0:
    print(number, "is multiple of 5")
else:
    print("Not the multiple of 5")
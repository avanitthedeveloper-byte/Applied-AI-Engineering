# Q1.
'''
salary = int(input("Enter your exact salary: "))

if salary < 30000:
    print("Tax Rate: 5%")
    print("Tax Amount:", salary*0.05)
elif salary >= 30000 and salary <= 70000:
    print("Tax Rate: 15%")
    print("Tax Amount:", salary*0.15)
else:
    print("Tax Rate: 25%")
    print("Tax Amount:", salary*0.25)
'''

# Q2.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))

def print_even(num1, num2):
    for val in range(num1, num2+1, 1):
        if val%2 == 0:
            print(val)

print_even(num1, num2)
'''

# Q3.
'''
num = int(input("Enter a number: "))

def print_digit(num):
    num1 = 0
    while num > 0:
        num1 = (num1 * 10) + (num%10)
        num = int(num/10)
    while num1 > 0:
        print(num1%10, end=" ")
        num1 = int(num1/10)
    print()
print_digit(num)
'''

# Q4.
'''
num = int(input("Enter a number: "))

def count_digits(num):
    num1 = num
    count = 0
    while num1 > 0:
        count += 1
        num1 = int(num1/10)
    print(count)

count_digits(num)
'''

# Q5.
'''
num = int(input("Enter a number: "))

def count_digits(num):
    num1 = num
    sum = 0
    while num1 > 0:
        sum += num1%10
        num1 = int(num1/10)
    print(sum)

count_digits(num)
'''

# Q6.
'''
num = int(input("Enter a number: "))

def div_by(num):
    for val in range(1, num+1, 1):
        if val%3 == 0 and val%15 == 0:
            print(val)

div_by(num)
'''

# Q7.
'''
while True:
    inp = input("Enter number of 'Quit': ")
    if inp == "Quit":
        print("Quited Successfully...")
    elif int(inp)%2 == 0:
        print(inp,"Is Even")
    else:
        print(inp,"Is Odd")
'''

# Q8.
'''
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
ops = input("Enter Operation: ")

def calculator(num1, num2, ops):
    match ops:
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "*":
            return num1*num2
        case "/":
            return num1/num2
        case _:
            return "Something went wrong!"

print(calculator(num1, num2, ops))
'''

# Q9.
'''
import math

num = int(input("Enter a number: "))

def is_prime(num):
    for val in range(2, num, 1):
        if num%val == 0:
            return False
    return True

print(is_prime(num))
'''

# Q10.
'''
while True:
    ans = 89
    num = int(input("Enter a number: "))
    if num == ans:
        print("Correct")
        break
    elif num > ans:   
        print("Input is Too High")
    else:
        print("Input is too low")
print("Game Over")
'''
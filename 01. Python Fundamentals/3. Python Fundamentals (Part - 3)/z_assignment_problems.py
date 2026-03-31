# Q1. 
'''
str = input("Enter a String: ")

i = 0
j = len(str)-1

while True:
    if str[i] != str[j]:
        print("Not a Palindrome")
        break
    elif i > j:
        print("Palindrome")
        break
    else:
        i += 1
        j -= 1
'''

# Q2.
'''
my_list = [98, 99, 92, 94]
sum = 0
for el in my_list:
    sum += el
print(f"Average: {round(sum/len(my_list), 2)}")
'''

# Q3.
'''
list1 = []
while True:
    num = input("Enter number or 'Quit': ")
    if num == "Quit":
        break
    else:
        list1.append(int(num))
list2 = []
while True:
    num = input("Enter number or 'Quit': ")
    if num == "Quit":
        break
    else:
        list2.append(int(num))
result_set = set()
result = []
for val in list1:
    result_set.add(val)
for val in list2:
    result_set.add(val)
for val in result_set:
    result.append(val)
result.sort()
print(result)
'''

# Q4.
'''
int_tup = [1,3,2,4,6,7,4,5,6,7]

int_odd = []

int_even = []

for val in int_tup:
    if val%2 == 0:
        int_even.append(val)
    else:
        int_odd.append(val)
print(f"Input: {int_tup}")

print(f"Even: {int_even}")

print(f"Odd: {int_odd}")
'''

# Q5.
'''
info = {}

def add_data():
    new_info = {input("Enter Name: ") : int(input("Enter marks: "))}
    info.update(new_info)
    print("\nData added successfully...\n")

def update_mark(sname):
    info.update({
        sname : int(input("Enter marks: "))
    })
    print("\nMarks updated successfully...\n")

def search_for_stu(sname):
    if info.get(sname) != None:
        print(f"Name: {sname}")
        print(f"Marks: {info[sname]}")


while True:
    ch = input("----- Choose The Following Option -----\nA - Add Student\nB - Update Marks\nC - Search for a Student\nD - Display all students and marks\nE - Exit\n")
    match ch:
        case "A":
            add_data()
        case "B":
            sname = input("Enter name: ")
            if info.get(sname) != None:
                update_mark(sname)
            else:
                print(f"{sname} doesn't exist in Database...")
        case "C":
            sname = input("Enter name: ")
            search_for_stu(sname)
        case "D":
            print(f"\n{info}\n")
        case "E":
            print("\nExited Successfully...\n")
            break
        case _:
            print("\nSomething went wrong. Please try again...\n")
'''

# Q6.
'''
fruits = ["apple", "banana", "kiwi", "cherry", "mango"]

info = {}

for fruit in fruits:
    info.update({
        fruit : len(fruit)
    })
print(info)
'''

# Q7.
'''
string = input("Enter String: ")

no_of_space = 0

for val in string:
    if val == " ":
        no_of_space += 1
print(no_of_space)
'''

# Q8.
'''
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

set1 = set()
set2 = set()

for ele in list1:
    set1.add(ele)
for ele in list2:
    set2.add(ele)

if len(set1.intersection(set2)) != 0:
    print("Some Common Element(s)")
else:
    print("No common elements")
''' 

# Q9.
'''
list = [1, 3, 7, 9, 6, 5, 2, 3, 6, 6]

my_set = set()

for val in list:
    ini_size = len(my_set)
    my_set.add(val)
    fin_size = len(my_set)
    if ini_size == fin_size:
        print(val, end=" ")
print()
'''

# Q10.
'''
string = input("Enter a String: ")
my_set = set()
for val in string:
    my_set.add(val)
print(my_set)
print(len(my_set))
'''
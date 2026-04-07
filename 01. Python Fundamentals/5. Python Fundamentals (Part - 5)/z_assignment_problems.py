# Q1.
'''
for i in range(5):
    data = input(f"Enter {i+1} name: ")
    with open("names.txt", "a+") as f:
        f.write(data)
        f.write("\n")
with open("names.txt", "r") as f:
    print(f.readlines())
'''
'''
with open("names.txt", "w") as f:
    for i in range(5):
        data = input(f"Enter {i+1} name: ")
        f.write(data + "\n")

with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())
'''
# Q2. 
'''
with open("log.txt", "a") as f:
    for i in range(3):
        data = input(f"Enter {i+1} log: ")
        f.write(data + "\n")
with open("log.txt", "r") as f:
    for line in f:
        print(line.strip())
'''
# Q3.
'''
my_list = [5, 10, 15, 20, 25]

my_new_list = [val for val in my_list if val > 15]

print(my_new_list)
'''

# Q4.
'''
import json

my_dict = {
    "pondicherry": 55000,
    "delhi": 90000,
    "patna": 75000
}

with open("cities.json", "w") as f:
    json.dump(my_dict, f, indent=4)

with open("cities.json", "r") as f:
    data = json.load(f)
    print(data)

name = input("City: ")
pop = int(input("Population: "))

data.update({
    name: pop
})

with open("cities.json", "w") as f:
    json.dump(data, f, indent=4)
'''

# Q5.
try:
    with open("data.txt", "r") as f:
        print("File Opend")
except:
    print("Unknown error caught")
else:
    print("File not found")
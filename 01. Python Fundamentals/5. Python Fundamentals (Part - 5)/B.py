# 2. perations on Files
'''
f = open("B.txt", "r")

data = f.read()

print(data)

f.close()
'''

'''
f = open("B.txt", "r")

data1 = f.readline()

print(data1)

data1 = f.readline()

print(data1)

print(type(data1))

f.close()
'''
f = open("B.txt", "r")

data = f.read()

print(data)

f = open("B.txt", "w")

f.write("Hello Cipher")

f = open("B.txt", "r")

data = f.read()

print(data)

f.close()


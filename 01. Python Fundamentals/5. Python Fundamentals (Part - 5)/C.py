# 3. Modes in File Operations

# r - Reading (default)
'''
f = open("C.txt", "r")

data = f.read()

print(data)

f.close()
'''

# w - Writing, truncate file first
'''
f = open("C.txt", "w")

f.write("All Indians are my brothers and sisters.")

f = open("C.txt", "r")

data = f.read()

print(data)

f.close()
'''

# x - Create new & open for writing
'''
f = open("test.txt", "x")

f.write("This is new file. ")
'''

# a - Writing, appends at end
'''
f = open("test.txt", "a")

f.write("I am 'a' that will write and appendat end")

f.close()
'''

# b - Binary Mode

# t - Text Mode

# + - Opens disk file for update (r & w)
'''
f = open("last.txt", "r+") 

f.write("123")

print(f.read())

f.close()
'''
'''
f = open("last.txt", "w+") 

f.write("123")

print(f.read())

f.close()
'''

f = open("last.txt", "a+") 

f.write("123")

print(f.read())

f.close()
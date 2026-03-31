# 3. String Formatting - f-string & format()
# # format() 
'''
a = 5
b = 13
sum = a + b
print("Sum of {} & {}: {}".format(a, b, sum))
'''

# Index Based Formatting
'''
a = 5
b = 13
sum = a + b
print("Sum of {1} & {0}: {2}".format(a, b, sum))
'''

# Value Based Formatting
'''
print("Sum of {a} & {b}: {sum}".format(a = 5, b = 13, sum = a+b))
'''

# # f-strings

a = 5
b = 13

print(f"Sum of {a} & {b} is {a+b}")
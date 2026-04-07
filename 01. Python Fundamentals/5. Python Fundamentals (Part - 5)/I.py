# 9. List Comprehensions
'''
squares = []

for i in range(0, 6, 1):
    squares.append(i*i)
print(squares)

squares = [i*i for i in range(6) if(i%2 != 0)] 

print(squares)
'''

'''
num = [-2, -4, 3, 5, 2, -1]

print(num)

num = [0 if val < 0 else val for val in num]

print(num)
'''

words = ["Hello", "Python", "CipherMind"]
print(words)
words = [word.upper() for word in words]
print(words)
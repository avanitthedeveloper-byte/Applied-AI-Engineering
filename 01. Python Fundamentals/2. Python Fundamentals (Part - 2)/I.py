# 9. Break & Continue Keyword

number = int(input("Enter a number: "))

i = 1

'''
while i <= number:
    if i%6 == 0:
        break
    else:
        print(i)
        i += 1

'''

'''
while i<= number:
    if i % 3 == 0:
        i += 1
        continue
    else:
        print(i)
        i += 1

'''

while i<= number:
    if i%2 == 0:
        i += 1
        continue
    else:
        print(i)
        i +=1
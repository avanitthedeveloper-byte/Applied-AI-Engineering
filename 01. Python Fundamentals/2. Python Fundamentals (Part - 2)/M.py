# 13. Sum of N numbers

number = int(input("Enter a number: "))

sum = 0

for i in range(1, number+1, 1):
    sum += i

print("Sum:", sum)
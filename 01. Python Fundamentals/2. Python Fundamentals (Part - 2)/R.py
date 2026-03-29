# 18. Factorial of N

# num = int(input("Enter a number: "))

# def factorial(num):
#     ans = 1
#     a = 1
#     while a <= num:
#         ans *= a
#         a += 1
#     return ans

# print("Factorial of", num,":", factorial(num))


num = int(input("Enter a number: "))

def factorial(num):
    ans = 1
    while num>0:
        ans *= num
        num -= 1
    return ans

print("Factorial of", num,":", factorial(num))
# 8. "finally" Keyword
try:
    x = int(input("Enter First number: "))
    y = int(input("Enter Second number: "))
    result = x/y
except ZeroDivisionError:
    print(f"Second number should not be Zero.")
except ValueError:
    print(f"Input is wrong.")
else:
    print(f"{x} divided by {y} is: {result}")
finally:
    print("I will always work.")
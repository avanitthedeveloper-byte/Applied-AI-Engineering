# 8. Tuple Methods

marks = (98, 96, 99, 91, 93, 99, 99)
sum = 0
for mark in marks:
    print(mark, end=" ")
    sum += mark
print(f"\nSum of {marks} is: {sum}")


print(f"Index: {marks.index(99)}")

print(f"Count: {marks.count(99)}")
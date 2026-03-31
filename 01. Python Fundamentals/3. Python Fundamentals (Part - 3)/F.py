# 6. Using Loops with Lists
'''
marks = [98, 96, 99, 91, 93]

for mark in marks:
    print(mark, end=" ")
print()
'''

marks = [98, 96, 99, 91, 93]
idx = 0
for mark in marks:
    if mark == 91:
        print(f"{mark} is at Index: {idx}")
        break
    idx += 1
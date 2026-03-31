# 13. Practice Problem (Part a & b)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# List all unique course
unique_course = set()

for key in info:
    unique_course.add(key[1])

print(unique_course)

# List students enrolled in English
for key in info:
    if key[1] == "English":
        print(key[0], end=" ")
print()

# 14. Practice Problem (Part C)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

my_dict = {}

for name, course in info:
    if(my_dict.get(name) == None):
        my_dict.update({
            name : set()
        })
        my_dict[name].add(course)
    else:
        my_dict[name].add(course)
print(f"My Dictinary: {my_dict}")
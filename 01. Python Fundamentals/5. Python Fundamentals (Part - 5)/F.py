# 6. Practice Problem
# Word Search
data = True
line = 0
word = "Python"
with open("f.txt", "r") as f:
    while data:
        data = f.readline()
        line += 1
        if(word in data):
            print(f"{word} present at line {line}")
            break
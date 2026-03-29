# 11. Vowel Count

string = input("Enter a string: ")

count = 0

for ch in string:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1
print("Total number of vowel:", count)
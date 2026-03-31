# 12. Set Methods

my_set1 = {2, 3, 6, 9, 3, 4, 2, 4, 5}

my_set2 = {2, 3, 5, 9, 24, 13, 8}

print(f"First Set: {my_set1}")
print(f"Second Set: {my_set2}")

my_set1.add(20)

print(f"First Set: {my_set1}")

my_set1.remove(20)

print(f"First Set: {my_set1}")

'''
my_set1.clear()
'''

'''
print(f"First Set: {my_set1}")

print(my_set2)
print(my_set2.pop())
print(my_set2.pop())
print(my_set2.pop())
print(my_set2.pop())
print(my_set2.pop())
print(my_set2.pop())
print(my_set2.pop())

'''

print(f"Union of {my_set1} & {my_set2} will be: {my_set1.union(my_set2)}")

print(f"Union of {my_set1} & {my_set2} will be: {my_set1.intersection(my_set2)}")
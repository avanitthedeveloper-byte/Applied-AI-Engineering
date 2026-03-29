# 15. Practice Examples (Functions)
'''
def avg_of_three_num(a, b, c):
    return (a+b+c)/3

print("Average: ", round(avg_of_three_num(2,3,15), 2))
'''

# Default value of Parameter (Last parameter should be default only)
def avg_of_three_num(a, b, c = 15):
    return (a+b+c)/3

print("Average: ", round(avg_of_three_num(2,3), 2))
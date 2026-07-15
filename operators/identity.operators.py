#Python Identity Operators 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

"""
Output:
True
False
True
"""

#Difference Between is and ==
#is - checks if both varaibles point to the same object in memory
#== - checks if the values of both varaibles are equal

#Eksemepel:

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
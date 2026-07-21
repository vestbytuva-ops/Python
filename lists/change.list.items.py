#Python - Change List Items:

"""
To change the value of a specific item, refer to the index number:
"""

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Change a Range of Item Values:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

"""
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
"""

#Example:

"""
Change the second value by replacing it with two new values:
"""

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#Example

"""
Change the second and third value by replacing it with one value:
"""

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

#The insert() method inserts an item at the specified index:

"""
Example:
Insert "watermelon" as the third item:
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
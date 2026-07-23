#Add List Items:

#Append Items:
#Example:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Output: apple, banana, cherry, orange

#Insert Items:

thislist = thislist = ["apple", "banana", "cherry"]
thislist.append(1, "orange") #This inserts the item as the second position.
print(thislist) 

"""
Note: As a result of the examples above, the  lists will now contain 4 items.
"""

#Extend List:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #To append elements from another list to the current list, use the extend() method.
print(thislist)

#Add Any Iterable:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
print(thislist) 
#Remove List Items:

"""
Remove Specified Item

The remove() method removes the specified item.
"""

#Example:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#Example: 
"""
Remove the first occurrence of "banana" 
"""

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


#Remove Specified Index:

#Example:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #The pop() method removes the specified index.
print(thislist)

#Example:

thislist = ["apple", "banana", "cherry"]
thislist.pop() #If you do not specify the index, the pop() method removes the last item.
print(thislist)

#Example

"""
The del keyword also removes the specified index:
"""

thislist = ["apple", "banana", "cherry"]
del thislist[0] #Removes the first item.
print(thislist)


#Example

thislist = ["apple", "banana", "cherry"]
del thislist #Delete the entire list.

"""If i want to print this it will cause an error because the list is deleted and there is nothing to print."""





#Python Lists:

mylist = ["apple", "banana", "cherry"]

#Example:

thislist = ["apple", "banana", "cherry"]
print(thislist)


"""
Since lsits are indexed, lists can have items witht the same value:
"""

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #Print the number of items in the list: 


#List Items - Data Types

#Example:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Example:
list1 = ["abc", 34, True, 40, "male"]

#Example:

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #Output: <class 'list'>

#The list() Constructor 

#Example:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



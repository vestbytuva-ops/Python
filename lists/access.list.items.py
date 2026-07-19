#Python - Access List Items

#Access Items:

thislsit = ["apple", "banana", "cherry"]
print(thislist[1])


#Negative Indexing:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#Range of Indexes:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Return the third, fourth and fifth item.

#Example:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #This example returns the items from the beginning to, but NOT including, "kiwi".

#Example:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #This example returns the items from "cherry" to the end.

#Example:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #This example returns the items from "orange" (-4) to, but NOT including "mango" (-1).

#Example:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #Check if "apple" is present in the list.


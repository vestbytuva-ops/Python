#Loop Lists

#Loop Through a List:

#Example:
thislist = ["apple", "banana", "cherry"]
for x in thislist: 
  print(x) #Print all items in the list, one by one.


#Loop Through the Index Numbers:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) #Print all items by referring to their index number.


#Using a While Loop:

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist): #Print all items, using a while loop to go through all the index numbers.
  print(thislist[i])
  i = i + 1 


#Looping Using List Comprehension:
#List Comprehension offers the shortest syntax for looping through lists:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


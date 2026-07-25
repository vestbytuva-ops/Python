#List Comprehension:

#Example: Without List Comprehension.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #Prints a new list containing only the fruits witht the letter "a" in the name.

#Example: With List Comprehension you can do all that with only one line of code.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

"""
The Syntax: newlist = [expression for item in iterable if condition == True]
The return value is a new list leaving the old list unchanged.
"""

#Example:

newlist = [x for x in fruits if x != "apple"] #The condition if x != "apple" will return True for all elements other than "apple, making the new list contain all fruits except "apple".
#The condition is optional and can be omitted.

#Example:

newlist = [x for x in fruits] #With no if statement.


"""
Iterable
"""

#Example: The iterable can be any iterable object, like a list, tuple, set etc.

newlist = [x for x in range(10)] #You can use the range() function to create an iterable.

#Example:

newlist = [x for x in range(10) if x < 5] #Accept only numbers lower than 5.


"""Expression"""

#Example:

newlist = [x.upper() for x in fruits] #Set the values in the new lsit to upper case.


#Example:

newlist = ['hello' for x in fruits] #Set all values in the new list to 'hello'


#Example:

newlist = [x if x != "banana" else "orange" for x in fruits] #Return the item if it is not banana, if it is banana return orange.



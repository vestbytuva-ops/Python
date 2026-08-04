"""Python Tuples"""

#Example:

thistuple = ("apple", "banana", "cherry") #Tuples are used to store multiple items in a single variable.
print(thistuple) #Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set and Dictionary.
#A tuple a unchangeable
#Tuples are written with round brackets.

#Example: Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Example: Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Example: One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Example: Strings, int and booleans data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


#Example: A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")

#Example:

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) 

#Example: Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) #note the double round-brackets
print(thistuple) 
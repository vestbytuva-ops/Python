#Python Sort Lists:

#Example: Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#Example: Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


"""Sort Descending"""

#Example: Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


"""Customize Sort Function"""

#Example: Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


"""Case Insensitive Sort"""

#Example: By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


#Example:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
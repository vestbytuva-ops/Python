#List Comprehension:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #Prints a new list containing only the fruits witht the letter "a" in the name.



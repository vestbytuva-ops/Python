#Multiline Strings

#You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#You can use three single quotes:


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#Strings are Arrays


a="Hello, World!"
print(a[1])


for x in "banana":
    print(x)


a = "Hello, World!"
print(len(a)) #len() function returns the length of a string


txt = "The best things in life are free!"
print("free" in txt) #To check if a certain phrase or character is present in a string we can use the keyword in


txt="The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


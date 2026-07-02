print("Hello World!")

print("This is a sample Python script."); print("It demonstrates basic syntax and functionality.")

print('Hello World!') #In Python both single and double quotes can be used to define strings.

print("Hello World!", end=" ") #Use space for better readability
print("I will print on the same line.") #The end parameter in the print function allows us to control what is printed at the end of the output. By default, it is a newline character, but we can change it to a space or any other character.

print(1) #For numbers do not use quotes
print(3.14) #For floating-point numbers
print(True) #For boolean values
print (3+3) #For expressions, the result will be printed

print ("I am", 35, "years old.") #Combine text and numbers in one output by separating them with a comma.


"""
This is a multi-line comment in Python.
You can use it to add detailed explanations or temporarily disable code.
"""

x=5
y="John"
print(x)
print(y) #Variables can store different types of data, such as integers and strings.

x=4 #x is of type int
x="Sally" #x is now of type str
print(x)

#Casting

x=str(3)   # x will be '3'
w=int(3)   # y will be 3
z=float(3) # z will be 3.0


x=5
y="John"
print(type(x)) #Print the data type of x
print(type(y)) #Print the data type of y

#For instance, the output of the above code will be:
#<class 'int'> and <class 'str'>, indicating that x is an integer and y is a string.

#Important: Single and Double quotes are the same and viarables can be declared by either of them.

#Case-Sensitive:

a=4
A="Sally"
#A will not overwrite a 

Variable Names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


#Camel Case:

myVariableName = "John"

#Pascal Case:
MyVariableName = "John"

Snake Case:

my_variable_name = "John"


#Many values to multiple variables:

x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One value to multiple varaibles:

x = y = z = "Orange"
print(x)
print(y)
print(z)


#Unpack a collection:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Output Variables:

x="Python is awesome"
print(x)


x="Python"
y="is"
z="awesome"

print(x,y,z)


x="Python "
y="is "
z="awesome"

print(x + y + z)

"""
Without the space after "Python " and "is " the output would be "Pythonisawesome"
"""

x=5
y=10

print (x + y)


#In the print function, when you try to combine a string and a number witht the + operator, Python will give you an error.

x=5
y="John"
print(x + y) #This will give an error because you cannot concatenate a string and an integer directly.


x=5
y="John"
print(x, y) #This will work because the print function can handle multiple data types when separated by a comma.


#Python Global Variables:

x="awesome"

def myfunc():
    print("Python is " + x)

myfunc()



x="awesome"

def myfunc():
    x="fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)


#The global keyword

def myfunc():
    global x
    x="fantastic"

myfunc()

print("Python is " + x)

#To change a global variable inside a function, use the global keyword to declare which variable you want to change.

x="awesome"

def myfunc():
    global x
    x="fantastic"

myfunc()

print("Python is " + x)







🐍 Python Notes & Cheat Sheet

A personal collection of Python notes, mini-examples, and practice scripts covering the language fundamentals — from variables and data types to strings, lists, booleans, and operators. This README works as a quick-reference cheat sheet for everything in the repository, so you can look things up without digging through every file.

📚 Table of Contents
🧮 Variables
🔠 Data Types
🔢 Numbers
🔄 Casting
🔤 Strings
📋 Lists
✅ Booleans
⚙️ Operators
📖 Cheatsheet
📁 Repository Structure
🧮 Variables

File: variables.py · test.py

Notes on how Python variables are created, named, and scoped. Covers basic print() usage, single vs. multi-line comments, dynamic typing, case sensitivity, naming conventions, multiple assignment, unpacking, and the global keyword.

Key Concepts
Concept	Description
Dynamic typing	A variable's type is set automatically based on the assigned value
Case sensitivity	x and X are treated as two different variables
Naming styles	camelCase, PascalCase, snake_case
Multiple assignment	Assign several variables in one line
Unpacking	Assign values from a list/tuple to several variables at once
global keyword	Lets a function modify a variable defined outside its scope
Examples
python
# Many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"

# One value to multiple variables
x = y = z = "Orange"

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# Using the global keyword
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  # Python is fantastic

⬆️ Back to top

🔠 Data Types

File: data.types.py

Short example showing how to check the data type of a variable using type().

python
x = 5
y = 3.14
z = "Hello"

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
Function	Description
type()	Returns the data type of a value or variable

⬆️ Back to top

🔢 Numbers

File: numbers.py

Notes on Python's numeric types: scientific notation floats, complex numbers, converting between number types, and generating a random number with the random module.

Key Points
Topic	Description
Scientific notation	Floats can use e/E to indicate a power of 10 (35e3)
Complex numbers	Written with a j for the imaginary part (5j)
Random numbers	random.randrange(start, stop) picks a random number in a range
Examples
python
# Scientific notation
x = 35e3
y = 12E4
z = -87.7e100

# Complex numbers
x = 3 + 5j
y = 5j

# Random number between 1 and 9
import random
print(random.randrange(1, 10))

⬆️ Back to top

🔄 Casting

File: casting.py

Casting is used to explicitly convert a value from one data type to another.

Function	Description
int()	Converts a value into an integer
float()	Converts a value into a floating-point number
str()	Converts a value into a string
complex()	Converts a value into a complex number
Example
python
x = 1

a = float(x)  # 1.0
b = str(x)    # '1'

print(a)
print(b)

⬆️ Back to top

🔤 Strings

Folder: strings/

Notes covering string basics, concatenation, formatting, slicing, escape characters, and built-in string methods.

File	Covers
strings.py	Multiline strings, strings as arrays, len(), membership checks (in / not in)
concatenate.strings.py	Joining strings with +
format.strings.py	F-strings, placeholders, number formatting, math inside f-strings
slicing.strings.py	Slicing with [start:end] and negative indexes
modify.strings.py	Common string modification methods
escape.characters.py	Using \" to escape quotes inside a string
strings.methods.py	Full reference list of built-in string methods
code.challenge.py	Practice challenge combining slicing, .upper(), and f-strings
Important Methods
Method	Description
.upper()	Converts a string to upper case
.lower()	Converts a string to lower case
.strip()	Removes whitespace from the beginning/end of a string
.replace(old, new)	Replaces a value with another value
.split(sep)	Splits a string into a list
.capitalize()	Converts the first character to upper case
.count()	Counts occurrences of a specified value
.find()	Searches the string and returns the position found
.join()	Joins elements of an iterable into a string
.startswith() / .endswith()	Checks if a string starts/ends with a value
.isalpha() / .isdigit() / .isnumeric()	Checks the character composition of a string
.title()	Converts the first letter of every word to upper case
Examples
python
# Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Hello World

# F-strings
age = 36
txt = f"My name is John, I am {age}"
price = 59
txt = f"The price is {price:.2f} dollars"

# Slicing
b = "Hello World!"
print(b[2:5])   # llo
print(b[:5])    # Hello
print(b[-5:-2]) # Wor

# Modifying
a = "Hello World!"
print(a.upper())     # HELLO WORLD!
print(a.replace("H", "J"))  # Jello World!
print(a.split(","))  # ['Hello World!']

# Escape characters
txt = "We are the so-called \"Vikings\" from the north."

⬆️ Back to top

📋 Lists

Folder: lists/

Notes on creating, accessing, changing, looping through, sorting, copying, and joining lists, plus list comprehensions.

File	Covers
python.lists.py	Creating lists, duplicates, len(), mixed data types, list() constructor
access.list.items.py	Indexing, negative indexing, slicing a range of items
change.list.items.py	Changing item(s) by index, insert()
add.list.items.py	append(), extend(), adding any iterable
remove.lists.items.py	remove(), pop(), del, clear()
loop.lists.py	for loop, while loop, and list comprehension loops
sort.lists.py	sort(), descending sort, custom sort key, case-insensitive sort, reverse()
copy.lists.py	copy() method and the slice operator [:]
join.lists.py	Joining lists with +, a for loop, or extend()
list.comprehension.py	Full list comprehension syntax with condition and expression
list.methods.py	Full reference list of built-in list methods
Common Methods
Method	Description
append()	Adds an element at the end of the list
insert()	Adds an element at a specified position
extend()	Adds elements of an iterable to the end of the list
remove()	Removes the first item with the specified value
pop()	Removes the element at the specified position
clear()	Removes all elements from the list
sort()	Sorts the list
reverse()	Reverses the order of the list
copy()	Returns a copy of the list
count()	Returns the number of elements with a specified value
index()	Returns the index of the first matching element
Examples
python
# Access & slice
thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(thislist[1])     # banana
print(thislist[-1])    # kiwi
print(thislist[2:5])   # ['cherry', 'orange', 'kiwi']

# Add / remove
thislist.append("mango")
thislist.remove("banana")
thislist.pop()

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

# Sort
thislist = [100, 50, 65, 82, 23]
thislist.sort()
thislist.sort(reverse=True)

# Copy
mylist = thislist.copy()
mylist = thislist[:]

⬆️ Back to top

✅ Booleans

Folder: booleans/

Notes on True/False values, comparisons, bool() evaluation, and how functions can return booleans.

File	Covers
python.booleans.py	Comparisons, bool(), truthy/falsy values, isinstance(), boolean-returning functions
booleans.challenge.py	Practice challenge with comparisons and bool()
Key Points
Concept	Description
True / False	The two boolean values in Python
bool(value)	Evaluates any value and returns True or False
Falsy values	False, 0, "", (), [], {}, None
Truthy values	Almost everything else, including non-empty strings/collections
isinstance()	Checks if an object is of a specified type
Examples
python
print(10 > 9)   # True
print(10 == 9)  # False

# bool() evaluation
print(bool("Hello"))  # True
print(bool(15))       # True
print(bool(0))        # False
print(bool(""))       # False

# Functions returning a boolean
def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

# isinstance check
x = 200
print(isinstance(x, int))  # True

⬆️ Back to top

⚙️ Operators

Folder: operators/

Notes covering all the main operator categories in Python: arithmetic, assignment, comparison, logical, identity, membership, bitwise, precedence, and the ternary (conditional) expression.

File	Covers
python.operators.py	Basic use of the + operator
arithmethic.operators.py	+ - * / % ** // and float vs. floor division
assignment.operators.py	The walrus operator :=
comparison.operators.py	== != > < >= <= and chained comparisons
logical.operators.py	and, or, not
identity.operators.py	is vs ==
membership.operators.py	in / not in for lists and strings
bitwise.operators.py	&, |, ^ and binary representations
operator.precedence.py	Order of operations
ternary.operator.py	Conditional (ternary) expressions, chained ternaries
code.challenge.py	Practice challenge combining several operators
Operator Reference
Category	Operators
Arithmetic	+ - * / % ** //
Comparison	== != > < >= <=
Logical	and or not
Identity	is is not
Membership	in not in
Bitwise	& | ^
Assignment (walrus)	:=
Examples
python
# Arithmetic
x, y = 15, 4
print(x % y)   # 3   (modulus)
print(x // y)  # 3   (floor division)
print(x ** y)  # power

# Comparison chaining
x = 5
print(1 < x < 10)  # True

# Identity vs equality
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True  -> same values
print(x is y)  # False -> different objects in memory

# Bitwise
print(6 & 3)  # 2
print(6 | 3)  # 7
print(6 ^ 3)  # 5

# Ternary operator
num = 6
x = "WEEKEND" if num > 5 else "Workday"

# Walrus operator
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

⬆️ Back to top

📖 Cheatsheet

A compact, at-a-glance summary of every topic in this repository.

Topic	Key things to remember
🧮 Variables	Dynamic typing, case-sensitive, global for function scope, multiple/unpacked assignment
🔠 Data Types	type() to check a value's type
🔢 Numbers	int, float, complex, scientific notation (e), random.randrange()
🔄 Casting	int(), float(), str(), complex()
🔤 Strings	.upper(), .lower(), .strip(), .replace(), .split(), f-strings, slicing [start:end]
📋 Lists	append(), insert(), remove(), pop(), sort(), reverse(), copy(), list comprehension
✅ Booleans	True, False, bool(), truthy/falsy values, isinstance()
⚙️ Operators	+ - * / // % **, == != > < >= <=, and or not, is/is not, in/not in, & | ^, ternary x if cond else y
📁 Repository Structure
Python/
├── README.md
├── variables.py             # Variables, naming, scope, global keyword
├── data.types.py            # type() and basic data types
├── numbers.py                # Number types, conversion, random numbers
├── casting.py                # Explicit type conversion
├── test.py                   # Global keyword mini-example
├── strings/
│   ├── strings.py
│   ├── concatenate.strings.py
│   ├── format.strings.py
│   ├── slicing.strings.py
│   ├── modify.strings.py
│   ├── escape.characters.py
│   ├── strings.methods.py
│   └── code.challenge.py
├── lists/
│   ├── python.lists.py
│   ├── access.list.items.py
│   ├── change.list.items.py
│   ├── add.list.items.py
│   ├── remove.lists.items.py
│   ├── loop.lists.py
│   ├── sort.lists.py
│   ├── copy.lists.py
│   ├── join.lists.py
│   ├── list.comprehension.py
│   └── list.methods.py
├── booleans/
│   ├── python.booleans.py
│   └── booleans.challenge.py
└── operators/
    ├── python.operators.py
    ├── arithmethic.operators.py
    ├── assignment.operators.py
    ├── comparison.operators.py
    ├── logical.operators.py
    ├── identity.operators.py
    ├── membership.operators.py
    ├── bitwise.operators.py
    ├── operator.precedence.py
    ├── ternary.operator.py
    └── code.challenge.py
<div align="center">

📌 A personal, ever-growing collection of Python fundamentals — built while learning, used as a cheat sheet ever after.

</div>

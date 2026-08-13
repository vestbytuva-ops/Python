# Python

A personal collection of Python notes, mini-examples, and practice scripts covering the language fundamentals — from variables and data types to strings, lists, tuples, booleans, and operators — plus small hands-on projects. This README works as a **quick-reference cheat sheet** for everything in the repository, so you can look things up without digging through every file.

---

## Table of Contents

- [Variables](#variables)
- [Data Types](#data-types)
- [Numbers](#numbers)
- [Casting](#casting)
- [Strings](#strings)
- [Lists](#lists)
- [Booleans](#booleans)
- [Operators](#operators)
- [Tuples](#tuples)
- [Projects](#projects)
- [Cheatsheet](#cheatsheet)
- [Repository Structure](#repository-structure)

---

## Variables

**File:** [`variables.py`](./variables.py) · [`test.py`](./test.py)

Notes on how Python variables are created, named, and scoped. Covers basic `print()` usage, single vs. multi-line comments, dynamic typing, case sensitivity, naming conventions, multiple assignment, unpacking, and the `global` keyword.

### Key Concepts

| Concept | Description |
|---|---|
| Dynamic typing | A variable's type is set automatically based on the assigned value |
| Case sensitivity | `x` and `X` are treated as two different variables |
| Naming styles | camelCase, PascalCase, snake_case |
| Multiple assignment | Assign several variables in one line |
| Unpacking | Assign values from a list/tuple to several variables at once |
| `global` keyword | Lets a function modify a variable defined outside its scope |

### Examples

```python
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
```

[Back to top](#python-notes--cheat-sheet)

---

## Data Types

**File:** [`data.types.py`](./data.types.py)

Short example showing how to check the data type of a variable using `type()`.

```python
x = 5
y = 3.14
z = "Hello"

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
```

| Function | Description |
|---|---|
| `type()` | Returns the data type of a value or variable |

[Back to top](#python-notes--cheat-sheet)

---

## Numbers

**File:** [`numbers.py`](./numbers.py)

Notes on Python's numeric types: scientific notation floats, complex numbers, converting between number types, and generating a random number with the `random` module.

### Key Points

| Topic | Description |
|---|---|
| Scientific notation | Floats can use `e`/`E` to indicate a power of 10 (`35e3`) |
| Complex numbers | Written with a `j` for the imaginary part (`5j`) |
| Random numbers | `random.randrange(start, stop)` picks a random number in a range |

### Examples

```python
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
```

[Back to top](#python-notes--cheat-sheet)

---

## Casting

**File:** [`casting.py`](./casting.py)

Casting is used to explicitly convert a value from one data type to another.

| Function | Description |
|---|---|
| `int()` | Converts a value into an integer |
| `float()` | Converts a value into a floating-point number |
| `str()` | Converts a value into a string |
| `complex()` | Converts a value into a complex number |

### Example

```python
x = 1

a = float(x)  # 1.0
b = str(x)    # '1'

print(a)
print(b)
```

[Back to top](#python-notes--cheat-sheet)

---

## Strings

**Folder:** [`strings/`](./strings)

Notes covering string basics, concatenation, formatting, slicing, escape characters, and built-in string methods.

| File | Covers |
|---|---|
| [`strings.py`](./strings/strings.py) | Multiline strings, strings as arrays, `len()`, membership checks (`in` / `not in`) |
| [`concatenate.strings.py`](./strings/concatenate.strings.py) | Joining strings with `+` |
| [`format.strings.py`](./strings/format.strings.py) | F-strings, placeholders, number formatting, math inside f-strings |
| [`slicing.strings.py`](./strings/slicing.strings.py) | Slicing with `[start:end]` and negative indexes |
| [`modify.strings.py`](./strings/modify.strings.py) | Common string modification methods |
| [`escape.characters.py`](./strings/escape.characters.py) | Using `\"` to escape quotes inside a string |
| [`strings.methods.py`](./strings/strings.methods.py) | Full reference list of built-in string methods |
| [`code.challenge.py`](./strings/code.challenge.py) | Practice challenge combining slicing, `.upper()`, and f-strings |

### Important Methods

| Method | Description |
|---|---|
| `.upper()` | Converts a string to upper case |
| `.lower()` | Converts a string to lower case |
| `.strip()` | Removes whitespace from the beginning/end of a string |
| `.replace(old, new)` | Replaces a value with another value |
| `.split(sep)` | Splits a string into a list |
| `.capitalize()` | Converts the first character to upper case |
| `.count()` | Counts occurrences of a specified value |
| `.find()` | Searches the string and returns the position found |
| `.join()` | Joins elements of an iterable into a string |
| `.startswith()` / `.endswith()` | Checks if a string starts/ends with a value |
| `.isalpha()` / `.isdigit()` / `.isnumeric()` | Checks the character composition of a string |
| `.title()` | Converts the first letter of every word to upper case |

### Examples

```python
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
```

[Back to top](#python-notes--cheat-sheet)

---

## Lists

**Folder:** [`lists/`](./lists)

Notes on creating, accessing, changing, looping through, sorting, copying, and joining lists, plus list comprehensions.

| File | Covers |
|---|---|
| [`python.lists.py`](./lists/python.lists.py) | Creating lists, duplicates, `len()`, mixed data types, `list()` constructor |
| [`access.list.items.py`](./lists/access.list.items.py) | Indexing, negative indexing, slicing a range of items |
| [`change.list.items.py`](./lists/change.list.items.py) | Changing item(s) by index, `insert()` |
| [`add.list.items.py`](./lists/add.list.items.py) | `append()`, `extend()`, adding any iterable |
| [`remove.lists.items.py`](./lists/remove.lists.items.py) | `remove()`, `pop()`, `del`, `clear()` |
| [`loop.lists.py`](./lists/loop.lists.py) | `for` loop, `while` loop, and list comprehension loops |
| [`sort.lists.py`](./lists/sort.lists.py) | `sort()`, descending sort, custom sort key, case-insensitive sort, `reverse()` |
| [`copy.lists.py`](./lists/copy.lists.py) | `copy()` method and the slice operator `[:]` |
| [`join.lists.py`](./lists/join.lists.py) | Joining lists with `+`, a `for` loop, or `extend()` |
| [`list.comprehension.py`](./lists/list.comprehension.py) | Full list comprehension syntax with condition and expression |
| [`list.methods.py`](./lists/list.methods.py) | Full reference list of built-in list methods |
| [`code.challenge.py`](./lists/code.challenge.py) | Practice challenge: access, update, append, and remove items |

### Common Methods

| Method | Description |
|---|---|
| `append()` | Adds an element at the end of the list |
| `insert()` | Adds an element at a specified position |
| `extend()` | Adds elements of an iterable to the end of the list |
| `remove()` | Removes the first item with the specified value |
| `pop()` | Removes the element at the specified position |
| `clear()` | Removes all elements from the list |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the order of the list |
| `copy()` | Returns a copy of the list |
| `count()` | Returns the number of elements with a specified value |
| `index()` | Returns the index of the first matching element |

### Examples

```python
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
```

[Back to top](#python-notes--cheat-sheet)

---

## Booleans

**Folder:** [`booleans/`](./booleans)

Notes on `True`/`False` values, comparisons, `bool()` evaluation, and how functions can return booleans.

| File | Covers |
|---|---|
| [`python.booleans.py`](./booleans/python.booleans.py) | Comparisons, `bool()`, truthy/falsy values, `isinstance()`, boolean-returning functions |
| [`booleans.challenge.py`](./booleans/booleans.challenge.py) | Practice challenge with comparisons and `bool()` |

### Key Points

| Concept | Description |
|---|---|
| `True` / `False` | The two boolean values in Python |
| `bool(value)` | Evaluates any value and returns `True` or `False` |
| Falsy values | `False`, `0`, `""`, `()`, `[]`, `{}`, `None` |
| Truthy values | Almost everything else, including non-empty strings/collections |
| `isinstance()` | Checks if an object is of a specified type |

### Examples

```python
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
```

[Back to top](#python-notes--cheat-sheet)

---

## Operators

**Folder:** [`operators/`](./operators)

Notes covering all the main operator categories in Python: arithmetic, assignment, comparison, logical, identity, membership, bitwise, precedence, and the ternary (conditional) expression.

| File | Covers |
|---|---|
| [`python.operators.py`](./operators/python.operators.py) | Basic use of the `+` operator |
| [`arithmethic.operators.py`](./operators/arithmethic.operators.py) | `+ - * / % ** //` and float vs. floor division |
| [`assignment.operators.py`](./operators/assignment.operators.py) | The walrus operator `:=` |
| [`comparison.operators.py`](./operators/comparison.operators.py) | `== != > < >= <=` and chained comparisons |
| [`logical.operators.py`](./operators/logical.operators.py) | `and`, `or`, `not` |
| [`identity.operators.py`](./operators/identity.operators.py) | `is` vs `==` |
| [`membership.operators.py`](./operators/membership.operators.py) | `in` / `not in` for lists and strings |
| [`bitwise.operators.py`](./operators/bitwise.operators.py) | `&`, `\|`, `^` and binary representations |
| [`operator.precedence.py`](./operators/operator.precedence.py) | Order of operations |
| [`ternary.operator.py`](./operators/ternary.operator.py) | Conditional (ternary) expressions, chained ternaries |
| [`code.challenge.py`](./operators/code.challenge.py) | Practice challenge combining several operators |

### Operator Reference

| Category | Operators |
|---|---|
| Arithmetic | `+` `-` `*` `/` `%` `**` `//` |
| Comparison | `==` `!=` `>` `<` `>=` `<=` |
| Logical | `and` `or` `not` |
| Identity | `is` `is not` |
| Membership | `in` `not in` |
| Bitwise | `&` `\|` `^` |
| Assignment (walrus) | `:=` |

### Examples

```python
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
```

[Back to top](#python-notes--cheat-sheet)

---

## Tuples

**Folder:** [`tuples/`](./tuples)

Notes on tuples — one of Python's built-in collection types, alongside List, Set, and Dictionary. Unlike lists, tuples are unchangeable (immutable) once created, but they can still be "updated" indirectly by converting them to a list and back.

| File | Covers |
|---|---|
| [`python.tuples.py`](./tuples/python.tuples.py) | Creating tuples, duplicates, `len()`, single-item tuples (the trailing comma), mixed data types, the `tuple()` constructor |
| [`update.tuples.py`](./tuples/update.tuples.py) | "Updating" a tuple by converting it to a list, changing an item, and converting it back |

### Key Points

| Concept | Description |
|---|---|
| Immutability | Tuples cannot be changed after creation — no `append()`, `remove()`, or item assignment |
| Round brackets | Tuples are written with `()` instead of `[]` |
| Single-item tuple | Needs a trailing comma: `("apple",)` — without it, it's just a string in parentheses |
| `tuple()` constructor | Builds a tuple from another iterable, e.g. `tuple(("apple", "banana"))` |
| Workaround for "updating" | Convert to `list()`, modify, then convert back with `tuple()` |

### Examples

```python
# Creating a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))

# Single-item tuple needs a comma
thistuple = ("apple",)
print(type(thistuple))  # <class 'tuple'>

# Without the comma it is NOT a tuple
thistuple = ("apple")
print(type(thistuple))  # <class 'str'>

# tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))

# "Updating" a tuple via list conversion
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  # ('apple', 'kiwi', 'cherry')
```

[Back to top](#python-notes--cheat-sheet)

---

## Projects

**Folder:** [`projects/`](./projects)

Small, self-contained scripts that combine several of the concepts above into one working program.

| File | Description |
|---|---|
| [`morse.py`](./projects/morse.py) | Takes a sentence from the user and converts it into Morse code using a lookup dictionary |

### Morse Code Translator (`morse.py`)

Asks the user for a sentence, confirms the action, then converts every character to its Morse code equivalent using `MORSE_CODE_DICT.get(letter, letter)` inside a loop, and joins the results into a single string.

```python
sentence = input("Enter your sentence")
confirmation = input(f"Are you sure you want to transfer this sentence into morse?, {sentence} (Y / N)")

if confirmation.upper() == "Y":
    new_sentence = sentence.upper()

    morse_resultat = []
    for letter in new_sentence:
        code = MORSE_CODE_DICT.get(letter, letter)
        morse_resultat.append(code)

    morse_setning = ' '.join(morse_resultat)

    print(f"Here is your sentence converted into morse:, {morse_setning}")
else:
    print("Script is cancelled by user")
```

Key techniques used: dictionary lookups with `.get(key, default)` to avoid `KeyError` on characters without a Morse code (like spaces), building up a result list inside a `for` loop, and `' '.join()` to combine the list into a final string.

[Back to top](#python-notes--cheat-sheet)

---

## Cheatsheet

A compact, at-a-glance summary of every topic in this repository.

| Topic | Key things to remember |
|---|---|
| Variables | Dynamic typing, case-sensitive, `global` for function scope, multiple/unpacked assignment |
| Data Types | `type()` to check a value's type |
| Numbers | `int`, `float`, `complex`, scientific notation (`e`), `random.randrange()` |
| Casting | `int()`, `float()`, `str()`, `complex()` |
| Strings | `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, f-strings, slicing `[start:end]` |
| Lists | `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `copy()`, list comprehension |
| Booleans | `True`, `False`, `bool()`, truthy/falsy values, `isinstance()` |
| Operators | `+ - * / // % **`, `== != > < >= <=`, `and or not`, `is`/`is not`, `in`/`not in`, `& \| ^`, ternary `x if cond else y` |
| Tuples | `()`, immutable, single-item needs a comma `("x",)`, `tuple()`, update via `list()` conversion |
| Projects | Combine dictionaries, loops, `.get()`, and `.join()` into working scripts |

---

## Repository Structure

```
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
│   ├── list.methods.py
│   └── code.challenge.py
├── booleans/
│   ├── python.booleans.py
│   └── booleans.challenge.py
├── operators/
│   ├── python.operators.py
│   ├── arithmethic.operators.py
│   ├── assignment.operators.py
│   ├── comparison.operators.py
│   ├── logical.operators.py
│   ├── identity.operators.py
│   ├── membership.operators.py
│   ├── bitwise.operators.py
│   ├── operator.precedence.py
│   ├── ternary.operator.py
│   └── code.challenge.py
├── tuples/
│   ├── python.tuples.py
│   └── update.tuples.py
└── projects/
    └── morse.py
```

---

<div align="center">

*A personal, ever-growing collection of Python fundamentals — built while learning, used as a cheat sheet ever after.*

</div>

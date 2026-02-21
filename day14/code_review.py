"""
Technical Interview Review Session
Python Basics to Lists
Candidate: Goutham Sai
"""

# 1) Data Types
"""
Python has built-in data types:
int, float, str, bool, list, tuple, set, dict
Python is dynamically typed.
"""
x = 10
y = 3.14
name = "Sai"
flag = True


# 2) Type Casting
"""
Type casting converts one data type to another
using int(), float(), str()
"""
a = "10"
b = int(a)


# 3) Operators and Precedence
"""
Arithmetic: + - * / %
Comparison: == != > <
Logical: and, or, not
'and' has higher precedence than 'or'
"""
result = False and True or True


# 4) Conditional Statements
"""
Python uses if, elif, else
Indentation is mandatory
"""
num = 5
if num > 0:
    print("Positive")
else:
    print("Non-positive")


# 5) Loops
"""
For loop and While loop
"""
for i in range(5):
    print(i)

count = 3
while count > 0:
    count -= 1


# 6) Strings
"""
Strings are sequences of characters
Indexing starts from 0
Supports slicing
"""
text = "Python"
first_char = text[0]
slice_text = text[0:3]


# 7) String Slicing
"""
Syntax: string[start:stop:step]
"""
s = "Hello"
reverse = s[::-1]


# 8) Lists
"""
List is ordered, mutable, allows duplicates
"""
mylist = [1, 2, 3, 4]


# 9) Access and Modify List
"""
Access using index
Modify by assigning new value
"""
first_element = mylist[0]
mylist[1] = 10


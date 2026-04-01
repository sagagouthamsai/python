"""
a function is an block of code which is reusable,organized amd dynamic
we define a function using the syntax
def function_name():
    ***
"""
def greet(name):
    print("hello ",name)

greet("goutham")

#function with return value
#this returns a value but will not print i.e.more secure
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


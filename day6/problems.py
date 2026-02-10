#Create variables of type int, float, str, and bool.
x=1
y=10.5
z="hello"
b=True

#Print the datatype of a variable using Python.
print(type(x))

#Convert an integer into a float.
x=float(x)
print(type(x))
print(x)

#Convert a float into an integer.
print(type(y))
y=int(y)
print(y)
print(type(y))

#What is the datatype of:

x = "Hello World"
print(type(x))

#What is the datatype of:

x = 20.5
print(type(x))

#Check whether a variable is int using code.
a="hello"
b=100

if type(a) is int:
    print(f"yes {a} is an integer")
else:
    print("not an integer")

if type(b) == int:
    print(f"yes {b} is an integer")
else:
    print("not an integer")

#Add an integer and float — what datatype is the result?
c=x+y
print("type of x is ",type(x))
print("type of y is ",type(y))
print(c)


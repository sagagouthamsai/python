#type casting is the process of converting one data type to another data type
#in python we can use the built in functions to convert data type

#basic type casting
a=10
print(float(a))
print(str(a))       

#there are two types of type casting
#1. implicit type casting i.e automatic type conversion
#2. explicit type casting i.e. manual type conversion for this we use functions

print(complex(a))
#here the type is implicit because we are not using any function to convert the type of a variable

#explicit type casting
b=10.5
print(int(b))
print(str(b))
print(complex(b))

#Convert integer 10 → float.
x=10
print(type(x))
print(float(x))

#Convert float 9.8 → integer.
y=9.8
print(type(y))
print(int(y))

#Convert integer 25 → string.
a=25
print(str(a))

#Convert string "100" → integer → add 50.
b="100"
c=int(b)
print(c,c+50)

#Convert string "3.14" → float → multiply by 2.
d="3.14"
z=float(d)
print(z,z*2)

#Convert float 5.0 → complex.
e=5.0
print(complex(e))

#What happens when:
#int("abc")
#value error is resulted

#Convert complex → int (try and observe).
g=1+3j
#print(int(g))

#an type error has occured due to imcompatibility

#Convert boolean True → int.
h=True
print(int(h))

#Convert int 0 → bool.
i=0
print(bool(i))

#Predict output:

x = int(5.7) + float(3)
print(x, type(x))

#Take a number as string input → convert to int → print square.
j="15"
k=int(j)
print(k,k**2)

#bool as int
print(True + True)
print(False - True)
print(True * 10)

#spice case
print(int(-3.9))
print(float("4.2"))
print(round(2.7))
print(int("10.5")) # here erroe occur beacuse we can only convert one datatype at a time here we are trying to convert string to int but the string is in float format so it is not possible to convert it directly to int we need to convert it to float first and then to int

print(bool(complex(10,20)))
print(str(complex(2,3)))
x = complex(3,4)
print(x.real)
print(x.imag)


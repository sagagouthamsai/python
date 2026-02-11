#in python there are three different types of numbers (int,float,complex)

#int
x = 5
#float
y = 3.14
#complexz 
z = 2 + 3j

#type function is used to check the type of a variable
print(type(x)) 

#adding int and float
a= x + y
print(a)
print(type(a))

#Multiply a complex number with 2
b=z * 2            #  * is used for multiplication
print(b)

#What is datatype of:
x=5 / 2             #  / gives actual answer 
print(x)
print(type(x))

#What is datatype of:

c=5 // 2           # // gives quotient without decimal part i.e rounded    It is called as floor division
print(c)
print(type(c))

#Find power: 2³ using Python
d=2**3
print(d)           # ** is used for power

#Convert negative float -3.9 to integer
e=int(-3.9)
print(e)           # int() is used to convert float to int


print(-5 // 2)

#spice cases
print("10" + "20")
print(int("10") + int("20"))


a = 10
b = 10
print(a is b)
print(id(a))
print(id(b))

x = 10000
y = 10000
print(x is y) #it is ture because of the small integer caching in python
print(id(x))
print(id(y))

print(0.1 + 0.2 == 0.3) #it is false because of the floating point precision issue in python    

x = complex(2,3)
y = int(5)
print(x + y)

print(complex(2,3) + True)





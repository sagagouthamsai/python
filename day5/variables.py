#a variable is mutable entity that can hold a value of any data type

a=10  #a is an variable
print(a) 

a=20
print(a)  #the value of a is changed to 20 i.e mutable

b="goutham"  
print(b)  #variable with character data type

a,b,c=10,20,30  #multiple variable assignment
print(a)
print(b)  
print(c)
print(a,b,c)

x=y=z=10  #multiple variable assignment with same value
print(x)
print(y)  
print(z)
print(x,y,z)

print(id(a))  #id() function returns the memory address of the variable

print(type(a))  #type() function returns the data type of the variable

#biginner's level bug
a = [1,2,3]
b = a
b.append(4)
print(a)  # changed too 
print(b)  # changed 

#solution to above bug
a = [1,2,3]
b = a.copy()  # creates a copy of the list
b.append(4) 
print(a)  # unchanged
print(b)  # changed

#hence int is not mutable it creates new memory location 
a = 10
b = a
print(id(a), id(b))   # same
a = 20
print(id(a), id(b))   # different

#Tuple Concatenation
t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)

#Tuple Repetition
tuple1=(7,8)
print(tuple1*4)

#Built-in Functions
t = (5,10,15,20)
print(max(t))
print(min(t))
print(sum(t))

#Count Occurrences
tuple2 = (1,2,2,3,2,4)
print(tuple2.count(2))

#Find Index
tuple3 = (10,20,30,40)
print(tuple3.index(30))

#Try changing the first element of a tuple (10,20,30).
tuple4=(10,20,30)
#tuple4[0]=100

#Tuple Packing
non_packed_tuple=1,2,3,4,5,6
print(non_packed_tuple)

#Tuple Unpacking
a,b,c=tuple4
print(a)
print(b)
print(c)

#Swap Using Tuple Unpacking
num1 = 10
num2 = 20
print(num1)
print(num2)
num1,num2=num2,num1
print(num1)
print(num2)

#Convert List to Tuple to list
list1=[1,2,3,4]
converted_tuple=tuple(list1)
print(converted_tuple)
reverse_conversion=list(converted_tuple)
print(reverse_conversion)

#Create a tuple with 5 numbers and print the third element.
mytuple=(1,2,3,5,5)
print(mytuple[2])

#Write a program to count how many times 5 appears in a tuple.
print(mytuple.count(5))

#Concatenate two tuples.
concattup=(1,2,3)
mytuple=mytuple+concattup
print(mytuple)

#Convert a list into a tuple.
list_tuple=list(mytuple)
print(list_tuple)

#Convert a tuple into a list.
converted_tuple=tuple(list_tuple)
print(converted_tuple)

#Write a program to unpack (10,20,30) into three variables.
packed=10,20,30
1,2,3==packed
print(1)
print(2)
print(3)

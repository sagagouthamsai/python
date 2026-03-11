#Create a tuple with 5 numbers and print the third element.
mytuple=(1,2,3,5,5)
#length of the tuple
print(len(mytuple))

#Tuple Slicing
tuple1=(10,20,30,40,50,60)
print(tuple1[:3])
print(tuple1[-3:])
print(tuple1[1:4])

#Check whether 15 exists in the tuple.
test_tuple=(5,10,15,20,25)

if 15 in test_tuple:
    print("yes")
else:
    print("no")

#print all elements
for char in mytuple:
    print(char)

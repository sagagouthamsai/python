#Create a set with the elements {10, 20, 30, 40} and print it.
example_set = {10,20,30,40}
print(example_set)

#Create a set from the list [1,2,2,3,4,4,5].Print the set and explain the output.
list_set=set([1,2,2,3,4,4,5])
print(list_set)

#Write a program to add an element 50 to the set {10,20,30,40}.
example_set.add(50)
print(example_set)

#Write a program to remove element 30 from the set {10,20,30,40}.
example_set.remove(30)
print(example_set)

#Write a program to check whether an element exists in a set.
"""input_value=int(input("Enter the element : "))
if input_value in example_set:
    print("yes")
else:
    print("no")
"""
#Create an empty set and add elements 5,10,15.
empty_set=set()
empty_set.update({5,10,15})
print(empty_set)

#Write a program to find the length of a set without using len().
length=0
for items in example_set:
    length+=1
print(length)


#set element modification is not posible but we can add or remove elements

#set addion
example_set={1,2,3,"apple","banana"}
example_set.add("added")
print(example_set)

#update sets
#we use update to add two sets i.e concatination,also we can add iterable using this

example_set1={5,6,7}
(example_set.update(example_set1))
print((example_set))

#remove an element in set
# we can use remove or discard.

#remove ,if element is not present then error occurs
example_set.remove(1)
#example_set.remove(10)
#discard ,if element is not present this does not give error
example_set.discard("added")
example_set.discard("10") 

#clear, we use  this method to delete all the elements in the set
example_set.clear()
print(example_set)

#del keyword is used to delete the whole sets from entire memory
#del(example_set)
#print(example_set)

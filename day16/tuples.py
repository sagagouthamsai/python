#an tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#tuples are written with round brackets
thistuple = ("apple", "banana", "cherry","grapes", "kiwi",)
print(thistuple)
#tuples allow duplicate values
thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)   

#we can also use the tuple() constructor to make a tuple
thistuple2 = tuple(("apple", "banana", "cherry"))
print(thistuple2)

#access tuple items by referring to the index number, inside square brackets
print(thistuple[1])

#negative indexing means start from the end
print(thistuple[-1])

#length of tuple
print(len(thistuple))

#we can also use the range of indexes by specifying where to start and where to end the range
print(thistuple[2:5])

#range of negative indexes
print(thistuple[-4:-1])

#we cannot change the value of tuple items, but we can convert the tuple into a list, change the list, and convert it back into a tuple
x = list(thistuple)
x[1] = "orange"
thistuple = tuple(x)
print(thistuple)



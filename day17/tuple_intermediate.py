#add items to a tuple
#we can add items into a tuple by converting it into a list and then converting it back into a tuple
thistuple = ("apple", "banana", "cherry","grapes", "kiwi")
y = list(thistuple)
y.append("grapes")
thistuple = tuple(y)
print(thistuple)

#another way to add items to a tuple is to concatenate with another tuple
thistuple = thistuple + ("mango ",)
print(thistuple)

#remove items from a tuple
z = list(thistuple)
z.remove("grapes")
thistuple = tuple(z)
print(thistuple)

#another way to remove items from a tuple is to concatenate with another tuple that does not contain the item to be removed
#remove kivi from the tuple
print(thistuple)
thistuple = thistuple[:3] + thistuple[4:]
print(thistuple)

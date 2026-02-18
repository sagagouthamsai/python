#sorting in list
#in list we use sort function to sort all the elements int he list
fruits = ["sai","zedra","apple","kiwi", "banana", "cherry"]

fruits.sort()
print(fruits)

#sort in reverse order
fruits.sort(reverse=True)
print(fruits)

#custom sorting
#we can also sort the list based on the length of the string
fruits.sort(key=len)
print(fruits)

#sorting is case sensitive
thislist = ["banana", "apple", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


#tuple looping 
#we use for and while loops to access the elements in the tuple
tupl = ("apple", "banana", "cherry")
for x in tupl:
    print(x)

#we can also use while loop to access the elements in the tuple
i = 0
while i < len(tupl):
    print(tupl[i])
    i += 1

#we can also use the range() function to access the elements in the tuple
for i in range(len(tupl)):
    print(tupl[i])


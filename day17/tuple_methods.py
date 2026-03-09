#Tule only has two built-in methods: count and index
my_tuple = (1, 2, 3, 4, 5, 1, 2)

#count() method returns the number of times a specified value appears in the tuple
print(my_tuple.count(1)) 
print(my_tuple.count(2))

#index() method returns the index of the first occurrence of a specified value in the tuple
print(my_tuple.index(1))
print(my_tuple.index(2))
#.
#finding duplicate values in a tuple using count() method
my_tuple = (1, 2, 3, 4, 5, 1, 2)
print("---------------------------------------------------")
for item in my_tuple:
    if my_tuple.count(item) > 1:
        print(my_tuple[item])
.
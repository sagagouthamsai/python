#list reversal
#reverse : it is used to reverse the order of the list
lst=[1,2,"a","b","hello"]
lst.reverse()
print(lst)

#list copy
#copy : it is used to create a copy of the list
lst1=lst.copy()
print(lst1)

#we can also use slicing or list constructor to copy a list
lst2=lst[:]
lst3=list(lst)
print(lst2)
print(lst3)

#list slicing
#slicing is used to access a range of elements in the list
#basic syntax : list_name[start:stop:step]
lst=[1,2,"a","b","hello"]
print(lst[1:4]) 

#list index function
#index : it is used to find the index of the first occurrence of an element in the list
lst=[1,2,"a","b","hello"]
print(lst.index("a")) 


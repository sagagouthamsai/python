#inserting into list
#insert method is used to insert elements into list 
#we can insert element at any position

#basic syntax : list_name.insert(position,element)
lst=[1,2,"a","b","hello"]
a=[3,4]
lst.insert(-1,a)
print(lst)

#append it is used to add elements at the end of the list
lst.append("hi")
print(lst)

#extend : it is used to add lists to list
#basic syntax
lst1=[3,4]
lst.extend(lst1)
print(lst)

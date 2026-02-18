#remove :it is used to remove items from the list from a specified item
lst=[1,2,"a","b","hello"]
lst.remove(1)
print(lst)

#pop : it is used to remove items using specific index or even last item from the lst
#last element
lst.pop()
print(lst)

#poping index no 3 element
print("element in index no 3 : ",lst[3])
lst.pop(3)
print(lst)

#we can use del instead of pop
del lst[0]
print(lst)

#clear : delets all the elements in the list,But not list.
lst.clear()
print(lst)
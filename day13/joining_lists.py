#joining two lists
#we can join two lists using + operator or extend method
#using + operator
lst1=[1,2,3]
lst2=[4,5,6]
lst3=lst1+lst2
print(lst3)

#using extend method
lst1=[1,2,3]
lst2=[4,5,6]
lst1.extend(lst2)
print(lst1)


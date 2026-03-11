#Write a program to find the largest element in a tuple without using max().
test_tuple=(4,8,2,10,6)
list_conv=list(test_tuple)
list_conv.sort()
print(list_conv[-1])

#Remove Duplicates from Tuple
org_tuple=(1,2,2,3,3,4,5)
new_tuple=()
for i in org_tuple:
    if org_tuple.count(i)==1:
        new_tuple+=(i,)
    else:
        continue
print(new_tuple)

#Nested Tuple Access
nested_tuple= (1,(2,3),(4,5,6))
#Print:3,5
print(nested_tuple[1][1],nested_tuple[2][1])

#Count Even Numbers
tuple_all=(1,2,3,4,5,6,7,8)
count=0
for num in tuple_all:
    if num%2==0:
        count+=1
print(count)

#Reverse a Tuple
list_tuple=list(tuple_all)
list_tuple.reverse()
tuple_conversion=tuple(list_tuple)
print(tuple_conversion)

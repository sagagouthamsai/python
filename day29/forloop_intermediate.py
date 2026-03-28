#Find Second Largest Number in a List
numbers = [10, 45, 32, 67, 89, 54]
print(sorted(numbers)[-2])

#Remove Duplicates from List (Without set())
Input= [1,2,2,3,4,4,5]
op=[]
for i in Input:
    if i not in op:
        op.append(i)
print(op)

#Find Common Elements Between Two Lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]
common_lst=[]
for val in list1:
    if val in list2:
        common_lst.append(val)
print(common_lst)

#Count Frequency of Each Element in List
list_value=[1,2,2,3,3,3]
fre_dict={}
for val in list_value:
    if val not in fre_dict:
        fre_dict[val]=list_value.count(val)
print(fre_dict)

#Find Prime Numbers from 1 to N
n=10

for i in range(n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print(i)

n=153
len_value=len(str(n))
a=[]
for i in str(n):
    a.append(int(i)**int(len_value))
if sum(a)==n:
    print("Armstrong Number")
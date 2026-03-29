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

#Find Missing Number in List
input_value=[1,2,3,5]
for i in range(input_value[0],input_value[-1]):
    if i not in input_value:
        print(i)

#Print Fibonacci Series Using For Loop
n=7
a,b=0,1
for i in range(1,n):
    print(a,end=" ")
    a,b=b,a+b
print(" ")

#Find All Pairs With Given Sum
input_list=[1,2,3,4,5]
target_sum=6
pairs=[]
for i in input_list:
    for j in range(i+1,len(input_list)):
        if i+input_list[j]==target_sum:
            pairs.append((i,input_list[j]))
print(pairs)

#Pattern — Number Triangle
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


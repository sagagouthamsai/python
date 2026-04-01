"""
#Count Words Frequency in a Sentence
sentenc="sai is good sai is smart"
op={}
for i in sentenc.split():
    if i not in op:
        op[i]=1
    else:
        op[i]=(sentenc.split()).count(i)
print(op)

#Move All Zeros to End of List
list1=[0,1,0,3,12]
temp=[]
temp1=[]
for i in list1:
    if i==0:
        temp.append(i)
    else:
        temp1.append(i)
temp1.extend(temp)
print(temp1)

#Find All Substrings of a String
Input="abc"
n=len(Input)
for i in range(n):
    for j in range(i+1,n+1):
        print(Input[i:j])

arr = [2, 3, 10, 6, 4, 8, 1]
res=[]
n=len(arr)
for i in range(n):
    print(arr[i]-arr[i])
    for j in range(i+1,n):
        res.append(arr[i]-arr[j])
print(min(res)*-1)   
"""

#Check if List is Sorted (Without sort())
s=[1,2,3,4,2,5]
n=len(s)
sorted=True
for i in range(1,n):
    if s[i]<s[i-1]:
        print("not sorted")
        sorted=False
        break

if sorted==True:
    print("sorted")

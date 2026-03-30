"""
low=3
high=7
count=0
for i in range(low,high+2):
    if i&1==0:
        count+=1
print(count)

a=34
b=6
ans=0
while a>0:
    ans+=(a%b)
    a=a//b
print(ans)

nums = [2,5,6,9,10]
nums=sorted(nums)
print(nums)
result=[]
for i in nums:
    if nums[0]%i==0 and nums[-1]%i==0:
        result.append(i)  
print(result[-1])
        
num=4
temp=[]
count=0
for i in range(1,num+1):
    for j in str(i):
        temp.append(int(j))
    if sum(temp)%2==0:
        print(i)
        count+=1
    temp.clear()
print(count)
"""

s = "IceCreAm"
S_list=list(s)
vowels="aeiouAEIOU"
right=0
left=len(s)-1
print(left)
while right<left:
    if S_list[right] not in vowels:
        right+=1
    elif S_list[left] not in vowels:
        left-=1
    else:
     S_list[right],S_list[left]=S_list[left],S_list[right]
     right+=1
     left-=1

print("".join(S_list))
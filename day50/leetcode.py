"""class Solution:
    def judgeCircle(self, moves: str) -> bool:
            x=0
            y=0
            for i in moves :
                if i == "U" :
                    y+=1
                elif i == "D" :
                    y-=1
                elif i == "R" :
                    x+=1
                elif i == "L" :
                    x-=1
            return x==y==0


s="RLRRLLRLRL"         
countr=0
countl=0
ans=0
l=len(s)
for i in range(l):
    if s[i]=="R":
        countr+=1
    elif s[i]=="L":
        countl+=1
    if countr==countl:
        print(countr,countl)
        ans+=1
            
print(ans)"""

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
res=[]
count=0
s=set(ar)
for i in s:
    res.append(ar.count(i))
    print(res,i)
for i in res:
    if i>2:
        count+=i
print(count//2)

def search(self, nums: List[int], target: int) -> int:
    l=len(nums)
    left=0
    right=l-1  

    while left <= right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
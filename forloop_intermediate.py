"""
low=3
high=7
count=0
for i in range(low,high+2):
    if i&1==0:
        count+=1
print(count)
"""
a=34
b=6
ans=0
while a>0:
    ans+=(a%b)
    a=a//b
print(ans)



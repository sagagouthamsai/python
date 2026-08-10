n=123456
count=0
while n:
    if (n%10)%2==0:
        count+=1
    n//=10
print(count)

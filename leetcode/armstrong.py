n=123

org=n
r=0
pwr=len(str(n))
while n>0:
    r+=(n%10)**pwr
    n//=10

if org==r:
    print("yes")

else:
    print("no")
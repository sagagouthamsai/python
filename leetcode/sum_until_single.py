n=9875
count=0
tot=0
while True:
    if n>0:
        tot+=n%10
        n//=10
    else:
        if tot>9:
            n=tot
            tot=0
            count+=1
        else:
            break
print(tot)
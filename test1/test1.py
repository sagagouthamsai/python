#problem 2


def magical_library(row,col,mat):
    res=0
    for i in range(row):
        temp=0
        for j in range(col):
            s=mat[i][j]
            if s%2!=0:
                temp+=s
        if temp%2==0 and temp:
            res+=1
    return res

r=magical_library( 3, 2, [[2,4],[0,0],[11,11]])
#print(r)


#problem 3
def ke(arr,n,s):
    arr=sorted(arr)
    left=0
    right=s-1
    p=0
    res=0
    output=0
    while left<right:
        if res<n:
            res+=arr[left]
            left+=1
        if res>n:
            while res>n:
                res-=arr[p]
                p+=1

        if res==n:
            output=max(output,left-p)
        
    return output

#print(ke( [4,2,3,1] ,5 ,4))

#p4
def dis(inp):
    freq={}
    res=0
    l=len(inp)
    for i in range(l):
        if inp[i] in freq:
            res=max(res,i-freq[inp[i]])
        
        freq[inp[i]]=i
    if not res:
        return len(inp)-1      
        
    return res-1

inp=dis("abc10")
#print(inp)

#p6
def red_green(ip1,ip2):
    res=0
    curr=1
    for i in ip2:
        if i%2!=curr:
            res+=1
    return res
#print(red_green(5 , {70,23,13,26,72,19}))
        
#p10
def srtstr(inp):
    srt=sorted(inp)
    res=0
    for i in range(len(inp)):
        if inp[i]!=srt[i]:
            res+=1
    return res
#print(srtstr("helco"))

#p11
def discounted(arr,n):
    s=sorted(arr)
    return sum(s[-n:])-s[-1]
#print(discounted( arr=[5,2,9,1,7,4,6], n=1))


#p13
def wave(pizza,puffs,coolds):
    print("No of pizzas:",pizza, "\nNo of puffs: ",puffs, "\n No of cooldrinks:",coolds)

    print("Total price =",pizza*100+puffs*20+coolds*10)

#w=wave(int(input("Enter no of pizzas : ")),int(input("Enter no of puffs : ")),int(input("Enter no of cool drinks : ")))
#print(w)

#p14
def palindrome(inp):
    c="Palindrome"
    if str(inp)[::-1]!=str(inp):
        c="Not a Palindrome"
    return c

#print(palindrome(212192))

#p15
def count(str):
    res=0
    spl=str.split(" ")
    for i in spl:
        res+=1
    return res
print(count("a is a cloud of b"))
def count(arr,exp):
    l=len(arr)
    cnt=[0]*10
    o=[0]*l

    for x in arr:
        num=x//exp
        cnt[x%10]+=1
    for i in cnt[1,10]:
        cnt[i]+=cnt[i-1]

    for i in reversed(arr):
        o[cnt[(i//exp)%10]-1]=i
        cnt[(i//exp)%10]-=1
    
    for i in range(l):
        arr[i]=o[i]

def radix(arr):
    exp=1
    m=max(arr)

    while m//exp>0:


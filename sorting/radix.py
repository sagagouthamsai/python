def count(arr,exp):
    l=len(arr)
    cnt=[0]*10
    o=[0]*l

    for x in arr:
        num=x//exp
        cnt[num%10]+=1
    for i in range(1,10):
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
        count(arr,exp)
        exp*=10

    return arr
arr=[1,99,999,3,4,2,1,111,2,3,66,5,44,111,1]
print(radix(arr))


def stbcnt(arr):
    m=max(arr)+1
    cnt=[0]*m
    res=[0]*len(arr)
    
    for i in arr:  #freq count
        cnt[i]+=1
    
    for i in range(1,m):  #prefix sum
        cnt[i]+=cnt[i-1]
        
    for i in reversed(arr):  #travesing
        res[cnt[i]-1]=i
        cnt[i]-=1
    return res


arr = [4,2,2,8,3,3,1]
print(stbcnt(arr))
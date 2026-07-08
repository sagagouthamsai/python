def cnt(arr):
    m=max(arr)+1
    cnt=[0]*m
    res=[]
    print("cnt",cnt,"m",m)
    for i in arr:
        cnt[i]+=1
    print("cnt",cnt)
    for v in range(len(cnt)):
        while cnt[v]>0:
            res.append(v)
            cnt[v]-=1

    return res

arr = [4,2,2,8,3,3,1]
print(cnt(arr))
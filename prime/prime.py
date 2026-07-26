def prime(n):
    if n<=2:
        return o
    p=[True]*n
    p[0]=False
    p[1]=False
    i=2
    while i*i<n:
        if p[i]:
            for j in range(i*i,n,i):
                p[j]=False
            i+=1
    res=[]
    for i in range(n):
        if p[i]:
            res.append(i)
    return res,sum(p)


print(prime(10))
def twoSum( numbers, target) :
    l=0
    r=len(numbers)-1
    while l<r:
        sum=numbers[l]+numbers[r]

        if sum == target:
            return [l+1,r+1]
        elif sum<target:
            l+=1
        else:
            r-=1
    return -1


print(twoSum(numbers=[2,7,11,15],target=9))


def is_prime(n):
    if n<=1:
        return []
    elif n==2:
        return [2]
    r=[2]
    s=3
    while s<n:
        c=True
        for i in range(2,int(s**0.5)+1,2):
            if s%i==0:
                c=False
                break
        if c:
        
            r.append(s)
        s+=2
    return r
print(is_prime(30))

             
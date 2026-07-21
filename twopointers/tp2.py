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
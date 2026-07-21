
def removeDuplicates( nums) :
    s=0
    l=len(nums)
    for i in range(1,l):
        if nums[s]!=nums[i]:
            s+=1
            nums[s]=nums[i]

    return s+1

print(removeDuplicates([1,1,2]))
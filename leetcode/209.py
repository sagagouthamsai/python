class Solution:
    def minSubArrayLen(self, target: int, nums: list()) -> int:
        b_m=float('inf')
        tot=0
        l=0
        for i in range(len(nums)):
            tot+=nums[i]
            while tot>=target:
                b_m=min(b_m,i-l+1)
                tot-=nums[l]
                l+=1
        return b_m if b_m!=float("inf") else 0
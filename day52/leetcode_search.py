#1920 — Build Array from Permutation
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
    
#1431 — Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = [True if i + extraCandies >= m else False for i in candies]
        return res
    
#1672 — Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0


        for amt in accounts:
            s = sum(amt)

            if res < s:
                res = s

        return res
    
#1773 — Count Items Matching a Rule
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        a = 0
        res = 0

        for i in items:
            if ruleKey == "type":
                a = 0

            if ruleKey == "color":
                a = 1

            if ruleKey == "name":
                a = 2

            if i[a] == ruleValue:
                res += 1

        return res
    
#2108 — Find First Palindromic String in the Array
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i

        return ""
    
#374 — Guess Number Higher or Lower
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n

        while l <= r:
            mid = (l + r) // 2
            res = guess(mid)

            if res == 0:
                return mid

            elif res == 1:
                l = mid + 1

            else:
                r = mid - 1

#704 — Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
    
#35 — Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left
    
#69 — Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid + 1

            else:
                right = mid - 1

        return right
        
#1365 — How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            count = 0

            for j in nums:
                if j < i:
                    count += 1

            res.append(count)

        return res

#Sort Without Using sort()
def manual_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):

            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

#75 -- Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums)

        for i in range(l):
            c = i

            for j in range(i + 1, l):
                if nums[c] > nums[j]:
                    c = j

            nums[i], nums[c] = nums[c], nums[i]

        return nums

#LeetCode #283 — Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums)
        p = 0

        for i in range(l):
            if nums[i] != 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        return nums
    
#202 — Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 0 and n not in s:
            s.add(n)

            sum = 0

            for i in str(n):
                sum += int(i) ** 2

            n = sum

        return n == 1
        

    
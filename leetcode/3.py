class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p=""
        r={}
        max_sub=0
        if len(s)==1:
            return 1

        for i in range(len(s)):
            if s[i] not in p:
                p+=s[i]
                r[s[i]]=i
            else:
                max_sub=max(max_sub,len(p))
                p= s[r[s[i]]+1:i+1]
                r[s[i]]=i

        max_sub=max(max_sub,len(p))
        return max_sub


#optimized version
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = 0
        r = {}
        max_sub = 0

        if not s:
            return 0

        for i in range(len(s)):
            if s[i] in r and p <= r[s[i]]:
                p = r[s[i]] + 1

            r[s[i]] = i
            max_sub = max(max_sub, i - p + 1)

        return max_sub


def countBits(self, n: int) -> List[int]:
    ans=[]
    for i in range(n+1):
        ans.append(bin(i).count("1"))
    return ans


def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        temp=[]
        for i in nums:
            if bin(i).endswith("0"):
                temp.append(i) 
        res=0
        for i in temp:
            res=res|i
        return res



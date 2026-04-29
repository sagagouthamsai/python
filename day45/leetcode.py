
def countBits(n: int) -> list[int]:
    ans=[]
    for i in range(n+1):
        ans.append(bin(i).count("1"))
    return ans


def evenNumberBitwiseORs( nums: list[int]) -> int:
        temp=[]
        for i in nums:
            if bin(i).endswith("0"):
                temp.append(i) 
        res=0
        for i in temp:
            res=res|i
        return res

print(countBits(8))

a=evenNumberBitwiseORs([1,2,3,4,5,6])
print(a)
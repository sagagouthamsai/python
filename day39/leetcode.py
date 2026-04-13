nums = [1] 
target = 1
start = 0

len_lst=len(nums)
temp=[]
temp1=[]
for i in range(len_lst):
    if target==nums[i]:
        temp.append(i)
for i in temp:
    temp1.append(abs(start-i))
print(min(temp1))
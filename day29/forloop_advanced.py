#Rotate List to the Right by K Steps
nums = [1,2,3,4,5]
k = 2
op=[]
for i in range(-k,(len(nums)-k)):
    op.append(nums[i])
print(op)

#Find Longest Word in a Sentence
Input_val="python is very powerful language"
op_lst={}
for i in Input_val.split():
    op_lst[i]=len(i)
max_value=max(op_lst.values())
for k,v in op_lst.items():
    if max_value==v:
        print(k)



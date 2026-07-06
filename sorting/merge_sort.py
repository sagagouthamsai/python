"""
def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    
    p=len(arr)//2
    left=merge_sort(arr[:p])
    right=merge_sort(arr[p:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
"""

def mergesort(arr):
    if len(arr)<=1:
        return arr
    p=len(arr)//2
    left=mergesort(arr[:p])
    right=mergesort(arr[p:])
    
    i=j=0
    res=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    while i<len(left):
        res.append(left[i])
        i+=1
        
    while j<len(right):
        res.append(right[j])
        j+=1

    return res
arr = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(arr))

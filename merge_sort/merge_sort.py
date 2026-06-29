def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    l=0
    r=len(arr)-1
    p=(l+r)//2
    left=arr[:p]
    right=arr[p:]


arr = [8, 3, 5, 1]

print(merge_sort(arr))
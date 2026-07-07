def bubble_sort(arr):
    l=len(arr)
    for i in range(l-1):
        for j in range(l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[85, 45, 92, 61, 70]
print(bubble_sort(arr))

def bubble(arr,n=len(arr)):
    if n<=1:
        return arr
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    bubble(arr,n-1)

arr = [7,2,9,4]

bubble(arr, len(arr))

print(arr)
    

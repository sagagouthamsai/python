def bubble_sort(arr):
    l=len(arr)
    for i in range(l-1):
        for j in range(l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[85, 45, 92, 61, 70]
print(bubble_sort(arr))
def par(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i+1

def qs(arr,low,high):

    if low<high:
        p=par(arr,low,high)
        p1=qs(arr,low,p-1)
        pr=qs(arr,p+1,high)
    return arr

arr=[1,99,999,3,4,2,1,111,2,3,66,5,44,111,1]
print(qs(arr,0,len(arr)-1))
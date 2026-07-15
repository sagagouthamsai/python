def qs(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return arr


arr=[1,99,999,3,4,2,1,111,2,3,66,5,44,111,1]
print(qs(arr,0,len(arr)-1))
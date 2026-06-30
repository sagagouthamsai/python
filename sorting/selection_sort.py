def selection(arr):
    l=len(arr)
    for i in range(l):
        m=i
        for j in range(i+1,l):
            if arr[m]>arr[j]:
                m=j
        arr[i],arr[m]=arr[m],arr[i]
    return arr
    
arr=[85, 45, 92, 61, 70]
print(selection(arr))
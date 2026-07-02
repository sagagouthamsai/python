def insertion_sort(arr):
    print(arr)
    l=len(arr)
    for i in range(1,l):
        k=arr[i]
        j=i-1
        print(f"i={i}\nk={k}\nj={j}")
        while j>=0 and arr[j]>k:
            print(f"j={j}\narr[j]={arr[j]} k={k} ")
            arr[j+1]=arr[j]
            print(arr)
            j-=1
        arr[j+1]=k
        print(arr)
    return arr


arr = [8, 3, 5, 1, 6]

print(insertion_sort(arr))

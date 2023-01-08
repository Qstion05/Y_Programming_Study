def InsertSort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]: #앞에 있는 요소가, 뒤에 있는 요소보다 클 경우
                arr[i - 1], arr[i] = arr[i], arr[i - 1] #SWAP


print(InsertSort([3,6,4,2,1,5]))
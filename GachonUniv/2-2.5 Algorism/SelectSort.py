def SelectSort(arr):
    for i in range(len(arr) - 1):
        min_idx = i

        for j in range(i + 1, len(arr)): # 최소값 탐색
            if arr[j] < arr[min_idx]: 
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i] # 최소값을 가진 인덱스와, 맨 앞 인덱스 스왑
        
arr = [5,3,4,2,1]
print(SelectSort(arr))
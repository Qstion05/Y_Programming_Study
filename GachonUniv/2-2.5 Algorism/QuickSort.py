def qsort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        qsort(arr, low, pivot - 1)   # 피벗은 맨 왼쪽, a[low]
        qsort(arr, pivot + 1, high)  # 피벗은 맨 왼쪽, a[pivot+1]

def partition(arr, pivot, high):  # 피벗 a[pivot]을 기준으로 좌우로 분할
    i = pivot + 1  # i는 피벗 바로 다음 숫자에서 시작하여 좌에서 우로
    j = high       # j는 맨 오른쪽에 있는 숫자에서 시작하여 우에서 좌로
    while True:
        while i < high and arr[i] <= arr[pivot]:  # 피벗보다 크면 정지
            i += 1

        while j > pivot and arr[j] > arr[pivot]:  # 피벗과 같거나 작으면 정지
            j -= 1

        if j <= i:  # 정지한 두 곳이 만나거나 지나쳤으면 루프에서 나간다.
            break
            
        arr[i], arr[j] = arr[j], arr[i]  # 정지된 두 곳의 숫자 교환
        i += 1
        j -= 1

    arr[pivot], arr[j] = arr[j], arr[pivot]  # a[j]와 a[pivot] 교환
    return j


input_list = [50, 80, 75, 30, 95, 90, 45, 10, 15, 70, 85, 30, 20, 50, 60]
print('정렬 전:\t', input_list)

qsort(input_list, 0, len(input_list) - 1)
print('정렬 후:\t', input_list)


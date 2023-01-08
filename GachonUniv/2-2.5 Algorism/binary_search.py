def binary_search(a, left, right, K): #이진탐색
	if right >= left: 
		mid = (left + right) // 2
		if a[mid] == K: #값이 같으면 탐색 종료
			return True
		elif a[mid] > K:  # 값이 K보다 클 경우, 왼쪽에서 탐색
			return  binary_search(a, left, mid-1,K)

		else: # 값이 K보다 작을 경우, 오른쪽에서 탐색
			return binary_search(a, mid+1, right, K)
	else:
		return False

arr = [10, 20, 25, 35, 45, 55, 60, 75, 85, 90]
n = len(arr)
print("값 55: ", binary_search(arr,0,n-1,55))
print("값 50: ", binary_search(arr, 0, n-1, 50))

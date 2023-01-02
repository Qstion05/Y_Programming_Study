#병합 정렬
#리스트를 중간을 기준으로 계속 쪼갠 뒤, 다시 병합하는 과정에서 비교를 통해 정렬하는 방법
#분할 정복 방법에 원리를 둠.


def MergeSort(arr): #재귀함수를 이용하여 리스트를 둘로 나누는 함수
	if len(arr) <= 1: 												#더이상 둘 로 나눌 수 없을 때
		return arr 													#해당 리스트를 반환한다.

	mid = len(arr)//2 #리스트의 중간지점
	left = arr[: mid] #처음부터, 중간까지의 리스트
	right = arr[mid:] #중간부터, 끝까지의 리스트
	left_arr = MergeSort(left) 										#재귀함수를 이용한 리스트 분할
	#print("left: ", left_arr)
	right_arr = MergeSort(right)
	#print("right: ", right_arr)
	return Merge(left_arr, right_arr) 

def Merge(left_arr, right_arr):# 리스트를 병합하면서 정렬하는 함수
	left = 0 #왼쪽 인덱스
	right = 0 #오른쪽 인덱스
	Merged_arr = []	#정렬된 리스트 
	while(left < len(left_arr) and right < len(right_arr)):			#한 쪽의 리스트에서, 값이 전부 정렬된 리스트로 배치 될 때 까지
		if left_arr[left] < right_arr[right]: 						#왼쪽 리스트의 left 인덱스 값보다, 오른쪽 리스트의 right 인덱스 값이 크면
			Merged_arr.append(left_arr[left]) 						#정렬된 리스트에 왼쪽 리스트의 left 인덱스 값을 먼저 넣고
			#print("값 비교, left < right")
			#print("Merged_arr: ", Merged_arr)
			left += 1 												#인덱스 숫자를 하나 올림.
		else:														#왼쪽 리스트의 left 인덱스 값보다, 오른쪽 리스트의 right 인덱스 값이 작으면
			Merged_arr.append(right_arr[right]) 					#정렬된 리스트에 오른쪽 리스트의 right 인덱스 값을 넣음
			#print("값 비교, left > right")
			#print("Merged_arr: ", Merged_arr)
			right += 1 												

	
	# 한쪽 리스트의 값이 모두 배치가 되면, 배치가 되지 않은 다른쪽의 리스트 값을 전부 배치함.

	if (left == len(left_arr)): 									#왼쪽 리스트의 값이 모두 배치 되었다면 
		while(right < len(right_arr)): 								#오른쪽 리스트의 값을 배치함.
			Merged_arr.append(right_arr[right])
			#print("값 배치")
			#print("Merged_arr: ", Merged_arr)
			right += 1
	else: 															#오른쪽 리스트의 값이 모두 배치되었다면
		while(left < len(left_arr)): 								#왼쪽 리스트의 값을 배치함
			Merged_arr.append(left_arr[left])
			#print("값 배치")
			#print("Merged_arr: ", Merged_arr)
			left += 1
	#print("Return arr: ", Merged_arr)
	return Merged_arr


arr = [1,3,5,2,6,4,8,7]
print("arr: ", arr)
print(MergeSort(arr))




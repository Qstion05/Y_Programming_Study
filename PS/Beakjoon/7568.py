'''
No:7568
Tier:Sliver 5
Name:덩치
Language:Python3
'''

#Code

N = int(input())
arr = [[0] * 2 for i in range(N)]
rank = []

for i in range(N):
	x, y = input().split()
	arr[i][0] = int(x)
	arr[i][1] = int(y)


for a in range(N):
	temp = 1
	for b in range(N):
		if int(arr[a][0]) < int(arr[b][0]) and int(arr[a][1]) < int(arr[b][1]):
			temp += 1
	rank.append(temp)
rank_str = " ".join(map(str, rank))
print(rank_str)

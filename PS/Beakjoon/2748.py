'''
No: 2748
Tier:Bronze 1
Name:피보나치 수 2
Language:Python3
'''



dynimic_list = [0] * 90
def pibonachi(n):
	global dynimic_list
	if n == 1 or n == 2:
		return 1

	if dynimic_list[n] != 0: #memoization
		return	dynimic_list[n]

	dynimic_list[n] = pibonachi(n-1) + pibonachi(n-2)
	return dynimic_list[n]

n = int(input())
print(pibonachi(n))

#time_out
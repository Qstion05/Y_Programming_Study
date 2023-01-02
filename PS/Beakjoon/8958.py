'''
No:8958
Tier: Bronze 2	
Name:OX퀴즈
Language:Python3
'''

#Code


test_case = int(input())
sum_score = 0
for i in range(test_case):
	OX_string = input()
	temp = 1
	for OX in OX_string:
		if OX == "O":
			sum_score += temp
			temp += 1
		else:
			temp = 1
	print(sum_score)




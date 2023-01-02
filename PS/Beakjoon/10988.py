'''
No:10988
Tier:Bronze 1
Name:펠린드롬인지 확인하기
Language:Python3
'''

#Code

str_a = input()
str_re = str_a[::-1]

if(str_a == str_re):
	print("1")
else:
	print("0")

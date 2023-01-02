import os, platform
print("카이사르 암호 해독기 입니다.")
print(" ")
cipher = input("암호화된 문자열을 입력하세요:")
void = input("공백을 처리할 문자를 입력하세요:")

if platform.system() == 'Windows':
	os.system('cls')
else:
	os.system('clear')

print("복호화 된 문장 모음")
for alphabet in range(26): #한칸씩 이동시킴.
	plain = ""
	for message in cipher: #cipher 문자열의 문자 하나하나 대응
		if ord(message) == 32:
			plain += void 
		elif ord(message) + alphabet > 90: # 아스키 코드값이 90이 넘으면, 65로 다시 돌아가서 계산
			plain += chr(ord(message) + alphabet - 26) 
		else:
			plain += chr(ord(message) + alphabet)
	print(alphabet, ":", plain)



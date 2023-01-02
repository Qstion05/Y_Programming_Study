import random


#로또 번호 생성 파트
def lotto_generator():
    lotto_number = []
    while len(lotto_number) != 7:
        new_number = random.randrange(1, 46)
        if new_number not in lotto_number:
            lotto_number.append(new_number)
    return lotto_number


#메인 파트

Lotto_list = [] 
n = int(input("출력할 갯수를 입력해 주세요"))
for i in range(n):
	temp = sorted(lotto_generator())
	if temp not in Lotto_list:
		Lotto_list.append(temp)
print(Lotto_list)

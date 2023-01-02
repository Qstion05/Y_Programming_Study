def Chg(x):
    temp = x*9.0/5.0 + 32
    return temp


while(True):
    C = float(input("섭씨 온도를 입력해주세요: "))
    F = Chg(C)
    print("C = ", end = "")
    print(C,end = "")
    print("-->", end = "")
    print("F = ",end = "")
    print(F)

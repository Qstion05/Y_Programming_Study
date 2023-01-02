def swap(x):
    Temp = x[0]
    x[0] = x[1]
    x[1] = Temp
    return x  #a,b = b,a 
    
a = input().split(' ')
print(a[0], a[1])
swap(a)
print(a[0], a[1])

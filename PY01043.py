def fullOfEven(x):
    for i in x:
        if int(i) % 2:
            return False
    return True

def mirror(i):
    i = str(i)
    return i+i[::-1]


t = int(input())
while t > 0:
    N = int(input())
    x = 1
    while True:
        if fullOfEven(str(x)):
            i = mirror(x)
            if int(i) >= N: break
            print(i, end=' ')
        x+=1
    print()
    t -= 1
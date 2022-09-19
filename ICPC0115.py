def factorial(n):
    fac =1
    while n != 0:
        fac *= n
        n -= 1
    return fac

def is_Krish(n):
    tmp = 0
    for i in n:
        tmp += factorial(int(i))
    if tmp == int(n):
        return 1
    return 0

t = int(input())
while t > 0:
    n = input()
    if(is_Krish(n)):
        print("Yes")
    else:
        print("No")
    t -= 1
def tn(n):
    n = str(n)
    s = n[::-1]
    if(n == s):
        return 1
    else:
        return 0

t = int(input())
while t > 0:
    n = int(input())
    for i in range(22, n):
        #print(s)
        #print(tn(i))
        if(tn(i) == 1):
          dem = 0
          ok = 1
          m = i
          while m != 0 :
             a = m % 10
             if a != 0 and a != 2 and a != 4 and a != 6 and a != 8:
              ok = 0
              break
             dem += 1
             m = int(m /10)
          if ok == 1 and dem % 2 == 0:
           print(i, end = ' ')
    print()
    t -= 1
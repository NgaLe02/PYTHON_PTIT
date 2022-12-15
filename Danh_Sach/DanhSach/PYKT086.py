x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWYXZ'

def solve(n, b):
    ans = ''
    while n > 0:
        ans += x[n % b]
        n = n // b
    print(ans[::-1])

f = open('C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\DanhSach\\DATA.in', 'r')

l = f.readlines()
t = int(l[0])

ind = 1
while t > 0:
    b = int(l[ind])
    ind += 1
    s = l[ind]
    ind += 1
    n = int(s, 2)
    solve(n, b)
    t -= 1
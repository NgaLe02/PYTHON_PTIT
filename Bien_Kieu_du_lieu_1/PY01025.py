s = input()
tmp = ''
dem = 0
for i in range (len(s) - 1, 0, -1):
    tmp += s[i]
    dem += 1
    if dem % 3 == 0:
        tmp += ','
tmp += s[0]
tmp = tmp[::-1]
print(tmp)
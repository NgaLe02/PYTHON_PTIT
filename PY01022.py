s = input()
change = 0
while len(s) > 1:
    sum = 0
    if s[0] == '-':
        sum += ord('-') - ord('0')
    else:
        sum += int(s[0])
    for i in range (1, len(s)):
        sum += int(s[i])
    s = str(sum)
    change += 1
print(change)
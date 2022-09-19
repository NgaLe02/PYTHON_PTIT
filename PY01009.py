s = input()
len = len(s)
dem = 0
for i in s:
    if i.islower() == True:
        dem += 1
if(dem >= len - dem):
    print(s.lower())
else:
    print(s.upper())
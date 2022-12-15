
class Team:
    def __init__(self, ma, ten, tenTruong):
        self.ma = "Team{:02d}".format(ma)
        self.ten = ten
        self.tenTruong = tenTruong

class ThiSinh:
    def __init__(self, ma, ten, Team):
        self.ma = "C{:03d}".format(ma)
        self.ten = ten
        self.Team = Team
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.Team.ten} {self.Team.tenTruong}"

a = []
t = int(input())
for i in range(t):
    a.append(Team(i + 1, input(), input()))

b = []
m = int(input())
for i in range(m):
    ten = input()
    maTeam = input()
    for j in a:
        if j.ma == maTeam:
            x = j
    b.append(ThiSinh(i + 1, ten, x))

b = sorted(b, key=lambda x:x.ten)
print(*b, sep='\n')
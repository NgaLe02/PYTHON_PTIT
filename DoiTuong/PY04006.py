import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        res = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return res


if __name__ == '__main__':

    t = int(input())
    arr = []
    for i in range(t):
        arr += [float(x) for x in input().split()]
    i = 0
    for index in range(t):
        p1 = Point(arr[i],arr[i + 1])
        p2 = Point(arr[i + 2],arr[i + 3])
        p3 = Point(arr[i + 4],arr[i + 5])
        d1 = p1.distance(p2)
        d2 = p1.distance(p3)
        d3 = p2.distance(p3)
        if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
            p = math.sqrt((d1 + d2 + d3) * (d1 + d2 - d3) * (-d1 + d2 + d3) * (d1 - d2 + d3))
            p /= 4
            p = format(p, ".2f")
            print(p)
        else:
            print("INVALID")
        i += 6
import math
from decimal import Decimal


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        res = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return res


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        p3 = Point(Decimal(arr[4]), Decimal(arr[5]))
        d1 = p1.distance(p2)
        d2 = p1.distance(p3)
        d3 = p2.distance(p3)
        if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
            p = d1 + d2 + d3
            p = format(p, ".3f")
            print(p)
        else:
            print("INVALID")
        t -= 1
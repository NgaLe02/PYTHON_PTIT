class Rectangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def perimeter(self):
        return (self.x + self.y) * 2

    def area(self):
        return self.x * self.y

    def color(self):
        return self.z.title()

    def isvalid(self):
        return self.x > 0 and self.y > 0


arr = input().strip().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.isvalid():
    print(r.perimeter(), r.area(), r.color())
else:
    print("INVALID")

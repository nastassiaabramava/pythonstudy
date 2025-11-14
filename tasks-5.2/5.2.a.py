class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, other):
        ans = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return round(ans, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            x, y = 0, 0
        elif len(args) == 1:
            x, y = args[0]
        else:
            x, y = args
        super(PatchedPoint, self).__init__(x, y)
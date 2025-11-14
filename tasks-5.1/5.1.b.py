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
class Rectangle:
    def __init__(self, first, second):
        (x1, y1), (x2, y2) = first, second
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        self.width = x2 - x1
        self.height = y2 - y1

    def perimeter(self):
        return round((2 * (self.width + self.height)), 2)
    def area(self):
        return round((self.width * self.height), 2)
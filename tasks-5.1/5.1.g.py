class Rectangle:
    def __init__(self, first, second):
        (x1, y1), (x2, y2) = first, second
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        self.width = round(x2 - x1, 2)
        self.height = round(y2 - y1, 2)
        self.left = (round(x1, 2), round(y2, 2))

    def get_pos(self):
        return self.left

    def get_size(self):
        return self.width, self.height

    def move(self, dx, dy):
        x, y = self.left
        self.left = (round(x + dx, 2), round(y + dy, 2))

    def resize(self, width, height):
        self.width = round(width, 2)
        self.height = round(height, 2)

    def perimeter(self):
        return round((2 * (self.width + self.height)), 2)

    def area(self):
        return round((self.width * self.height), 2)

    def turn(self):
        x, y = self.left
        self.center = (round(x + self.width / 2, 2), round(y - self.height / 2, 2))
        cx, cy = self.center
        self.width, self.height = self.height, self.width
        self.left = (round(cx - self.width / 2, 2), round(cy + self.height / 2, 2))

    def scale(self, factor):
        x, y = self.left
        self.center = (round(x + self.width / 2, 2), round(y - self.height / 2, 2))
        cx, cy = self.center
        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)
        self.left = (round(cx - self.width / 2, 2), round(cy + self.height / 2, 2))
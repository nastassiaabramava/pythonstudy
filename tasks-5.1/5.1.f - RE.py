class Rectangle:
    def __init__(self, first, second):
        (x1, y1), (x2, y2) = first, second
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        self.width = x2 - x1
        self.height = y2 - y1
        self.left = (x1, y2)

    def get_pos(self):
        x, y = self.left
        return round(x, 2), round(y, 2)

    def get_size(self):
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx, dy):
        x, y = self.left
        self.left = (x + dx, y + dy)

    def resize(self, width, height):
        self.width = width
        self.height = height
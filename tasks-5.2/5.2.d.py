class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            x, y = args
        # на случай строки с /
        elif len(args) == 1:
            val = args[0]
            if isinstance(val, str):
                # строка вида "a/b"
                a, b = val.split('/')
                x, y = int(a), int(b)
        # находим нод
        a, b = x, y
        while b != 0:
            a, b = b, a % b
        # делим числислитель и знаменатель на него (условие задачи)
        x //= a
        y //= a
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}/{self.y}'

    def __repr__(self):
        return f'Fraction({self.x}, {self.y})'

    def numerator(self, value=None):
        # когда все почистано, то просто возвращаем х
        if value is None:
            return abs(self.x)
        # если нам дали новый числитель, то ищем нод и делим на него
        # у остается прежним
        x, y = value, self.y
        a, b = x, y
        while b != 0:
            a, b = b, a % b
        x //= a
        y //= a
        self.x, self.y = x, y
        return abs(self.x)

    def denominator(self, value=None):
        # та же история, что для х, только для у
        if value is None:
            return abs(self.y)
        x, y = self.x, value
        a, b = x, y
        while b != 0:
            a, b = b, a % b
        x //= a
        y //= a
        self.x, self.y = x, y
        return abs(self.y)
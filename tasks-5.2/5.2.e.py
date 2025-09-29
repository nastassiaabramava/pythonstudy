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
        self._x, self._y = self._normalize(x, y)

    @staticmethod
    # тут будет эвклид, который нормализует наши числа
    def _normalize(x: int, y: int) -> int:
        a, b = abs(x), abs(y)
        while b != 0:
            a, b = b, a % b
        g = a or 1
        x //= g
        y //= g
        if y < 0:
            x, y = -x, -y
        return x, y

    def __str__(self):
        return f'{self._x}/{self._y}'

    def __repr__(self):
        return f"Fraction('{self._x}/{self._y}')"

    def numerator(self, value=None):
        # когда все почистано, то просто возвращаем х
        if value is None:
            return abs(self._x)
        # сохраняем отдельно знак дроби, и потом добавляем его к новому значению
        sign = -1 if self._x < 0 else 1
        new_x = sign * value
        self._x, self._y = self._normalize(new_x, self._y)
        return abs(self._x)

    def denominator(self, value=None):
        if value is None:
            return abs(self._y)
        self._x, self._y = self._normalize(self._x, value)
        return abs(self._y)

    def __neg__(self) -> 'Fraction':
        return Fraction(-self._x, self._y)
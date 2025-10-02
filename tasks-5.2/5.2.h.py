from functools import total_ordering


@total_ordering
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

    # формула эвклида
    @staticmethod
    def _gcd(a: int, b: int) -> int:
        a, b = abs(a), abs(b)
        while b != 0:
            a, b = b, a % b
        return a

    # формула нок
    @staticmethod
    def _lcm(a: int, b: int) -> int:
        return abs(a * b) // Fraction._gcd(a, b)

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __lt__(self, other):
        return self._x * other._y < other._x * self._y

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
        # та же история, что для х, только для у
        if value is None:
            return abs(self._y)
        self._x, self._y = self._normalize(self._x, value)
        return abs(self._y)

    def reverse(self):
        self._x, self._y = self._y, self._x
        self._x, self._y = self._normalize(self._x, self._y)
        return self

    def __str__(self):
        return f'{self._x}/{self._y}'

    def __repr__(self):
        return f"Fraction('{self._x}/{self._y}')"

    def __neg__(self) -> 'Fraction':
        return Fraction(-self._x, self._y)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        den = self._lcm(self._y, other._y)
        a = den // self._y
        b = den // other._y
        num = self._x * a + other._x * b
        return Fraction(num, den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        den = self._lcm(self._y, other._y)
        a = den // self._y
        b = den // other._y
        num = self._x * a - other._x * b
        return Fraction(num, den)

    def __iadd__(self, other: 'Fraction') -> 'Fraction':
        changed = self + other
        self._x, self._y = changed._x, changed._y
        return self

    def __isub__(self, other: 'Fraction') -> 'Fraction':
        changed = self - other
        self._x, self._y = changed._x, changed._y
        return self

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        num = self._x * other._x
        den = self._y * other._y
        return Fraction(num, den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        num = self._x * other._y
        den = self._y * other._x
        return Fraction(num, den)

    def __imul__(self, other: 'Fraction') -> 'Fraction':
        changed = self * other
        self._x, self._y = changed._x, changed._y
        return self

    def __itruediv__(self, other: 'Fraction') -> 'Fraction':
        changed = self / other
        self._x, self._y = changed._x, changed._y
        return self
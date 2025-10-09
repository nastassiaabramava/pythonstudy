class MyAwesomeError(Exception):
    pass


class NoSolutionsError(MyAwesomeError):
    pass


class InfiniteSolutionsError(MyAwesomeError):
    pass


def find_roots(a, b, c):
    if a == b == c == 0:
        raise InfiniteSolutionsError()
    if a == 0:
        if b == 0:
            raise NoSolutionsError()
    D = b * b - 4 * a * c
    if D > 0:
        s = D ** 0.5
        x1 = (-b - s) / (2 * a)
        x2 = (-b + s) / (2 * a)
        return (x1, x2)
    elif D == 0:
        return (-b / (2 * a), -b / (2 * a))
    elif D < 0:
        raise NoSolutionsError()
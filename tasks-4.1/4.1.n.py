def can_eat(horse, other):
    (hx, hy), (ox, oy) = horse, other
    if abs(hx - ox) * abs(hy - oy) == 2:
        return True
    else:
        return False
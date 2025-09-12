def is_prime(x):
    x2 = int(x ** 0.5)
    for i in range(2, x2 + 1):
        if x % i == 0 or x == 0:
            return False
    return True   # без else, чтобы проверить все делители на false
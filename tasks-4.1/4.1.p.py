def is_palindrome(x):
    if isinstance(x, str):
        a = x.lower()
        return a == a[::-1]
    elif isinstance(x, (list, tuple)):
        return x == x[::-1]
    else:
        a = str(x)
        return a == a[::-1]
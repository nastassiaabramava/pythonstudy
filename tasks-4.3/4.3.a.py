def recursive_sum(*args):
    if not args:
        return 0
    return recursive_sum(*args[:-1]) + args[-1]
print(recursive_sum(1, 2, 3))
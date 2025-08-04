from itertools import product
expr = input()

print('a b c f')

for a, b, c in product((0, 1), repeat=3):
    f = eval(expr, {}, {'a': bool(a), 'b': bool(b), 'c': bool(c)})
    print(a, b, c, int(f))

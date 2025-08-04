from itertools import product, repeat
n = int(input())
print('А Б В')
for a, b, c in product(range(1, n + 1), repeat=3):
    if a + b + c == n:
        print(a, b, c)

from itertools import product, repeat
n = int(input())
row = []
for i in product(range(1, n + 1), repeat=2):
    row.append(str(i[0] * i[1]))
    if len(row) == n:
        print(' '.join(row))
        row = []

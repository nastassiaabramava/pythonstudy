from itertools import product
n = int(input())
m = int(input())
row = []
max_w = len(str(n * m))
for i in product(range(1, n * m + 1)):
    row.append(f'{i[0]:>{max_w}}')
    if len(row) == m:
        print(' '.join(row))
        row = []

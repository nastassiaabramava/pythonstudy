from itertools import permutations
n = int(input())
row = []

for _ in range(n):
    row.extend(input().replace(',', '').split())

for i in sorted(permutations(row, 3)):
    print(' '.join(i))

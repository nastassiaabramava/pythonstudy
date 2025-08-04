from itertools import permutations
n = int(input())
row = sorted([input() for i in range(n)])

for i in permutations(row):
    print(', '.join(i))

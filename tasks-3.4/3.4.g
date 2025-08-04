from itertools import combinations
n = int(input())
players = [input() for i in range(n)]

for a, b in combinations(players, 2):
    print(f'{a} - {b}')

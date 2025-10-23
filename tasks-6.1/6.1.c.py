import math

n = input().split()
for i in n:
    x = math.comb(int(n[0]), int(n[1]))
    y = math.comb((int(n[0]) - 1), int(n[1]) - 1)

print(y, x)

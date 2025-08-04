n = int(input())
m = int(input())
s = len(str(m * n))
a = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i % 2 != 0:
            a += 1 
            print(f'{a:>{s}}', end=' ')
        else:
            a = m * i + 1 - j
            print(f'{a:>{s}}', end=' ')
            a = a + m - 1
    print()

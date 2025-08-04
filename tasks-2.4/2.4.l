n = int(input())
m = int(input())
a = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        a += 1
        s = len(str(m * n))
        print(f'{a:>{s}}', end=' ')
        
    print()

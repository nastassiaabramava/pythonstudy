n = int(input())
m = int(input())
s = len(str(m * n))

for i in range(1, n + 1):
    a = i
    for j in range(1, m + 1):
        print(f'{a:>{s}}', end=' ')
        a += n 
    print()

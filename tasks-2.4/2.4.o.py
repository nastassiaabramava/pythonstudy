n = int(input())
m = int(input())
s = len(str(m * n))

for row in range(n):
    for col in range(m):
        number = (col * n + row + 1) if col % 2 == 0 else (col * n + n - row)
        print(f'{number:>{s}}', end=' ')
    print()
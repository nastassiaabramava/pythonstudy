n = int(input())
width = int(input())
sep = '-' * ((n * width) + (n - 1))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        number = f'{i * j:^{width}}'
        end = '|' if j != n else ''
        print(number, end=end)
    print()
    if i != n:
        print(sep)
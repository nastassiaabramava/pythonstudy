n = int(input())

# для выравнивания чисел в столбиках по центральному числу
center = (n + 1) // 2
width = len(str(center))

for row in range(n):
    for col in range(n):
        number = min(row + 1, col + 1, n - row, n - col)
        print(f'{number:>{width}}', end=' ')
    print()
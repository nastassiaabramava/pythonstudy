n = int(input())
m = int(input())

if m > n:
    for i in range(n, m + 1, 1):
        print(i, end=' ')
elif m < n:
    for i in range(n, m - 1, -1):
        print(i, end=' ')
else:
    print(n)

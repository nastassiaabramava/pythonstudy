n = input()
m = len(n)
max_n = 1

for i in range(m + 1):
    ld = int(n) % 10
    if ld > max_n:
        max_n = ld
    n = int(n) // 10
print(max_n)

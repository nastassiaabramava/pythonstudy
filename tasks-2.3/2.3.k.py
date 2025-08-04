n = input()
m = len(n)
sum = 0

for i in range(m + 1):
    ld = int(n) % 10
    sum += ld
    n = int(n) // 10
print(sum)

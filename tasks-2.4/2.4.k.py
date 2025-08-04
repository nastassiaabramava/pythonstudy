n = int(input())
a = n
sum1 = 0

for i in range(n):
    n = int(input())
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            sum1 += 1
            break
    if n == 1:
        sum1 += 1
sum = a - sum1
print(sum)

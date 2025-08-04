n = int(input())
sum = 0


for i in range(n):
    total = 0
    while (s := input()) != 'ВСЁ':
        if 'зайка' in s:
            total += 1     
    if total:
        sum += 1
print(sum)

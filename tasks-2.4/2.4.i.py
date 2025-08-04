n = int(input())

sum = ''

for i in range(n):
    s = str(input())
    max_x = 0
    for j in range(len(s)):
        ld = int(s) % 10
        if ld > max_x:
            max_x = ld
        s = int(s) // 10
    sum = str(sum) + str(max_x)
print(sum)

n = int(input())
fd = n // 100
sd = n // 10 % 10
ld = n % 10
x = max(fd, sd, ld)
y = min(fd, sd, ld)
sum1 = max(fd, sd, ld) + min(fd, sd, ld)
if fd != x and fd != y and fd * 2 == sum1:
    print('YES')
elif sd != x and sd != y and sd * 2 == sum1:
    print('YES')
elif ld != x and ld != y and ld * 2 == sum1:
    print('YES')
else:
    print('NO')

n = int(input())
flag = 'YES'
n2 = int(n ** 0.5)

for i in range(2, n2 + 1):
    if n % i == 0:
        flag = 'NO'
        break
if n == 1:
    print('NO')
elif 'NO' in flag:
    print('NO')
else:
    print('YES')

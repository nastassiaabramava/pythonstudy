n = int(input())
s1 = ''
s2 = n

while n != 0:
    ld = n % 10
    s1 += str(ld)
    n = n // 10
if str(s1) == str(s2):
    print('YES')
else:
    print('NO')

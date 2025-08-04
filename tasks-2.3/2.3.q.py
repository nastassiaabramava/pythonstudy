n = int(input())
s = ''
s2 = ''

while n != 0:
    ld = n % 10
    if ld % 2 != 0:
        s += str(ld)
    n = n // 10
while int(s) != 0:
    ld1 = int(s) % 10
    s2 += str(ld1)
    s = int(s) // 10
print(s2)

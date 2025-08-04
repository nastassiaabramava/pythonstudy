n = int(input())
m = int(input())
a = ''
b = []

for i in range(m + 1):
    s = input()
    a += s
    if len(a) + 3 < n:
        b.append(s)
    if len(a) + 3 == n:
        s = s + '...'
        b.append(s)
    if len(a) + 3 > n:
        x = (len(a) + 3) - n
        if x != len(s):
            y = (f'{s[0: - x]}...')
            b.append(y)
            break
        else:
            break
            
for j in range(len(b)):
    print(b[j])

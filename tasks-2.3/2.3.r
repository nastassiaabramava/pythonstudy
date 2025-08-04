n = int(input())
s = ''

for i in range(2, n + 1):
    if i % 2 != 0 or i == 2:
        x = i
    while n % x == 0:
        s += str(x) + ' * ' 
        n = n // x
print(s[:-2])

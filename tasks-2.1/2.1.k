n = int(input())
a = n // 1000
b = (n // 100) % 10
c = (n % 100) // 10
d = n % 10
print(b, a, d, c, sep='')

n = int(input())
m = int(input())
y = m * n

while m > n and m % n != 0:
    x = m % n
    m = n
    n = x
while m < n and n % m != 0:
    x = n % m
    n = m
    m = x
y1 = int(y / x)
print(y1)

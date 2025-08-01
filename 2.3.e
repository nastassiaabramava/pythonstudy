n = float(input())
count = 0

while n != 0:
    if n >= 500:
        n = n - n / 10
    count += n
    n = float(input())
print(count)

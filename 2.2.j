n = int(input())
fd = n // 100
sd = n // 10 % 10
ld = n % 10 

x = fd + sd
y = sd + ld
if x < y:
    print(y, x, sep='')
else:
    print(x, y, sep='')

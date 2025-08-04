n = int(input())
fd = str(n // 100)
sd = str(n // 10 % 10)
ld = str(n % 10)

x = fd + sd
y = fd + ld
z = sd + fd
w = sd + ld
q = ld + fd
r = ld + sd

if int(fd) == 0:
    num2 = min(z, w, q, r)
elif int(sd) == 0:
    num2 = min(x, y, q, r)
elif int(ld) == 0:
    num2 = min(x, y, z, w)
else:
    num2 = min(x, y, z, w, q, r)
num1 = max(x, z, y, w, q, r)

print(num2, num1, sep=' ')

s = input()
s = s.split()
ma = max(s)

for i in range(len(s)):
    a = s[i]
    while int(a) != 0 and int(ma) != 0:
        if int(a) >= int(ma):
            a = int(a) % int(ma)
        elif int(ma) > int(a):
            ma = int(ma) % int(a)
        x = int(a) + int(ma)
print(x)

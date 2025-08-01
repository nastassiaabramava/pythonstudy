s = input()
a = list(s)
b = []
d = []
sum = 0

for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        sum += 1
    else:
        b.append(a[i])
        d.append(sum + 1)
        sum = 0
       
b.append(a[i + 1])
d.append(sum + 1)
for j in range(len(b)):
    print(b[j], d[j])

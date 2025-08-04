n = int(input())
a = {}
d = []
sum = 0

for i in range(n + 1): 
    s = input()
    s = s.split()
    s1 = s.pop(0)
    a[s1] = s
k = s1

for name in a:
    if k in a[name]:
        d.append(name)
        d.sort()
        sum += 1
if sum == 0:
    print('Таких нет')
for i in d:
    print(i)

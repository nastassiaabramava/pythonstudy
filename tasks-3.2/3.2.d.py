n = int(input())
m = int(input())
a = set()
a1 = set()

for i in range(n):
    s = input()
    a.add(s)
for i in range(m):
    s1 = input()
    a1.add(s1)

all = a & a1
if len(all) > 0:
    print(len(all))
else:
    print('Таких нет')

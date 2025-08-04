n = int(input())
m = int(input())
a = set()
d = []

for i in range(n + m):
    s = input()
    a.add(s)
    d.append(s)
if len(a) == len(d):
    print(len(a))
elif len(d) / 2 == len(a):
    print('Таких нет') 
elif len(a) < len(d):
    print(len(d) - ((len(d) - len(a)) * 2))
else:
    print('Таких нет')

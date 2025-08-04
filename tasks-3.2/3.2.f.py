n = int(input())
m = int(input())
checker = set()
result = set()

for i in range(n + m):
    s = input()
    if s in checker:
        result.remove(s)
    else:
        checker.add(s)
        result.add(s)

if len(result) > 0:
    print('\n'.join(sorted(result)))
else:
    print('Таких нет')

from itertools import islice, cycle
m = int(input())
spisok = [input() for i in range(m + 1)]
n = int(spisok.pop())
result = list(islice(spisok, n))
s = []
for i in cycle(result):
    if len(s) < n:
        s.append(i)
    else:
        break
for i in s:
    print(i)

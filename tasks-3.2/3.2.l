n = int(input())
people = dict()
a = []

for i in range(n):
    name = input()
    people[name] = people.get(name, 0) + 1           
for name in people:
    if people[name] != 1:
        final = f'{name} - {people[name]}'
        a.append(final)
        a.sort()
    else:
        continue
if len(a) == 0:
    print('Однофамильцев нет')
for i in a:
    print(i)

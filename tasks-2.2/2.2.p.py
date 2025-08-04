p = int(input())
v = int(input())
t = int(input())

p1 = 'Петя'
v1 = 'Вася'
t1 = 'Толя'

max_s = max(p, v, t)
min_s = min(p, v, t)

if max_s == p:
    first = p1
    if min_s == v:
        third = v1
        second = t1
    else:
        third = t1
        second = v1
elif max_s == v:
    first = v1
    if min_s == p:
        third = p1
        second = t1
    else:
        third = t1
        second = p1
elif max_s == t:
    first = t1
    if min_s == p:
        third = p1
        second = v1
    else:
        third = v1
        second = p1


print(f'{first: ^24}')
print(f'{second: ^8}')
print(f'{third: >22}')
print('   II      I      III   ')

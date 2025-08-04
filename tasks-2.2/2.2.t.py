s1 = str(input())
s2 = str(input())
s3 = str(input())
z = 'зайка'

a = (f'{s1} {len(s1)}')
b = (f'{s2} {len(s2)}')
c = (f'{s3} {len(s3)}')

if z in a and z in b and z in c:
    print(min(a, b, c))
elif z in a and z in b:
    print(min(a, b))
elif z in a and z in c:
    print(min(a, c))
elif z in b and z in c:
    print(min(b, c))
elif z in a:
    print(a)
elif z in b:
    print(b)
elif z in c:
    print(c)

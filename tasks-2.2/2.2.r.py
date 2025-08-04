a = int(input())
b = int(input())
c = int(input())

max_s = max(a, b, c)
min_s = min(a, b, c)
ave_s = a + b + c - max_s - min_s

if max_s ** 2 == min_s ** 2 + ave_s ** 2:
    print('100%')
elif max_s ** 2 > min_s ** 2 + ave_s ** 2:
    print('велика')
elif max_s ** 2 < min_s ** 2 + ave_s ** 2:
    print('крайне мала')

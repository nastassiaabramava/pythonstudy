n = int(input())
all = set()


for i in range(n):
    object = input()
    o = object.split()
    a = set(o)
    all = all.union(a)
print('\n'.join(all))

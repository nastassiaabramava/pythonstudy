n = int(input())
m = int(input())
t = int(input())

x = n * 60 + m + t
y = x // 60 % 24
z = x % 60

print(f'{y:0>2}:{z:0>2}')

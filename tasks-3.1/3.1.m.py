n = int(input())
a = []

for i in range(n + 1):
    s = int(input())
    a.append(s)
p = a.pop()
for letter in a:
    x = letter ** p
    print(x)

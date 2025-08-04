n = int(input())
name = str(input())

for i in range(n - 1):
    s = str(input())
    if s < name:
        name = s
print(name)

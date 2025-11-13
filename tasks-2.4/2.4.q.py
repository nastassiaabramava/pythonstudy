n = int(input())
total = 0

for i in range(n):
    s = input()
    if s == s[::-1]:
        total += 1
print(total)
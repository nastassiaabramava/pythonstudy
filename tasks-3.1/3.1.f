n = int(input())
count = 0

for i in range(n):
    s = input()
    count += s.count('зайка')
print(count)

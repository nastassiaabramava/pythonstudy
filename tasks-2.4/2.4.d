n = int(input())
sum = 0

for i in range(n):
    s = int(input())
    s2 = str(s)
    for j in range(len(s2)):  
        s1 = s % 10
        sum += s1
        s = s // 10
print(sum)

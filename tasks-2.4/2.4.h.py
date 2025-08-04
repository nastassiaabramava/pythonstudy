n = int(input())
sum = 0
max_sum = 0
a = ''
b = ''
flag = False

for i in range(n):
    sum = 0
    s = str(input())
    n1 = int(input())
    n2 = str(n1)
    for j in range(len(n2)):
        ld = n1 % 10
        sum += ld
        if sum > max_sum:
            max_sum = sum
            a = s
            flag = True
        elif sum == max_sum:
            b = s
            flag = False
        n1 = n1 // 10
if flag:
    print(a)
else:
    print(b)

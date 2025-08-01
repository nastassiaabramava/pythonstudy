n = int(input())
num = 1
flag = False

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num += 1
        if num == n + 1:
            flag = True
            break
    if flag:
        break
    print()

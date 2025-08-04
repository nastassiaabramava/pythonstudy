n = int(input())

for i in range(n):
    s = input()
    k = s.find('за') + 1
    if 'за' not in s:
        print('Заек нет =(')
    else:
        print(k)

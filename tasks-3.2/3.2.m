n = int(input())
dishes = set()
menu = set()

for i in range(n):
    s = input()
    dishes.add(s)
days = int(input())
for k in range(days):
    num = int(input())
    for j in range(num):
        a = input()
        menu.add(a)
result = sorted(dishes ^ menu)
if not result:
    print('Готовить нечего')
else:
    for dish in result:
        print(dish)

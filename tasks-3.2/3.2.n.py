n = int(input())
products = set()
menu = []
recipes = dict()

for i in range(n):
    s = input()
    products.add(s)  
blocks = int(input())
for j in range(blocks):
    dish = input()
    if dish not in recipes:
        recipes[dish] = []
    for k in range(int(input())):
        ingred = input()
        recipes[dish].append(ingred)
    d = set(recipes[dish])
    d1 = d - products
    if not d1:
        menu.append(dish)
        menu.sort()
    else:
        continue
if not menu:
    print('Готовить нечего')
for i in menu:
    print(i)

from itertools import combinations, product
s = input()
n = input()
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
deck = [f'{rank} {suit}' for rank, suit in product(ranks, suits)]

spisok = [i for i in deck if n not in i]
valid_combos = []

for i in combinations(spisok, 3):
    combo = sorted(i)
    for j in combo:
        if s[:3] in j:
            combo_str = ', '.join(combo)
            if combo_str not in valid_combos:
                valid_combos.append(combo_str)
            else:
                continue
valid_combos.sort()            
for i in valid_combos[:10]:
    print(i)

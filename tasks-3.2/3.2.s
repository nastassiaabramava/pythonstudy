n = int(input())
kidtoys = {}

for kid in range(n):
    kid = input()
    k = kid.split()
    spisok = []
    for i in k:
        j = i.rstrip(':').rstrip(',')
        spisok.append(j)
    a = spisok[0]
    kidtoys[a] = spisok[1:] 
result = []
checker = []
for name in kidtoys:
    toys1 = kidtoys[name]
    toys = set(toys1)
    for toy in toys:
        if toy not in result:
            result.append(toy)
        else:
            checker.append(toy)
mn_result = set(result)
mn_checker = set(checker)
all = sorted(mn_result ^ mn_checker)
for toy in all:
    print(toy)

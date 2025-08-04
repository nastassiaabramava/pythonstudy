vse_s = []
digits = []
spisok = []


while (s := input()) != 'ФИНИШ':
    vse_s.append(s)
    spisok_s = ''.join(vse_s)
    k = spisok_s.lower()
    spisok_po_bukvam = list(k)
    spisok_po_bukvam.sort()
for letter in spisok_po_bukvam:
    if letter.isalnum and letter != ' ':
        spisok.append(letter)
    else:
        continue
for letter in spisok:
    count = spisok.count(letter)
    digits.append(count)
    m = max(digits)
    if spisok.index(letter) == digits.index(m):
        x = letter  
print(min(x))

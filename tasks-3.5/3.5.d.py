from sys import stdin
spisok = []
for i in stdin:
    i = i.rstrip()
    spisok.append(i)
x = spisok.pop()
    
for i in spisok:
    if x.lower() in i.lower():
        print(i)

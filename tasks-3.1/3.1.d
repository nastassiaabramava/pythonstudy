a = []

while (s := input()) != '':
    if not (s.endswith('@@@')):
        a.append(s)
for i in a:
    if i.startswith('##'):
        print(i[2:])
    else:
        print(i)

from sys import stdin

for i in stdin:
    i = i.rstrip()
    if not i.startswith('#'):
        if '#' in i:
            s = i.find('#')
            print(i[:s])
        else:
            print(i)

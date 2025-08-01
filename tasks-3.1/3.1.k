n = int(input())
a = []

for i in range(n + 1):
    s = input()
    a.append(s)  
x = a.pop()
for letter in a:
    if x.lower() in letter.lower():
        print(letter)
    else:
        continue

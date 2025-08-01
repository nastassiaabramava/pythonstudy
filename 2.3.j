x = 0
y = 0

while (s := str(input())) != "СТОП":
    n = int(input())
    if s == 'СЕВЕР':
        x += n
    elif s == 'ВОСТОК':
        y += n
    elif s == 'ЮГ':
        x -= n
    elif s == 'ЗАПАД':
        y -= n
print(x, y, sep='\n') 

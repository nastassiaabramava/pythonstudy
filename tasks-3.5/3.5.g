count = 0
positive = 0
spisok = []
with open(input(), encoding='UTF-8') as file_in:
    for i in file_in:
        for line in i.rstrip('\n').split(' '):
            num = int(line)
            spisok.append(num)
            count += 1
            if num > 0:
                positive += 1
num_min = min(spisok)
num_max = max(spisok)
suma = sum(spisok)
aver = suma / count 

print(count, positive, num_min, num_max, suma, f'{aver:.2f}', sep='\n')

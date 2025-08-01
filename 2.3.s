min_x = 0
max_x = 1001
x = 500

print(x)
while (answer := input()) != 'Угадал!':
        
    if answer == 'Меньше':
        max_x = x
        x = max_x - (max_x - min_x) // 2
        print(x)
    elif answer == 'Больше':
        min_x = x
        x = (max_x - min_x) // 2 + x
        print(x)

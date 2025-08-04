n = int(input())


for i in range(1, n + 1):
    
    for j in range(3 + i, 0, -1):
        s = j - 1
        if s == 0:
            break
        print(f'До старта {s} секунд(ы)')

    print(f'Старт {i}!!!')

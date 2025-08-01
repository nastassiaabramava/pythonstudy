names = {}

while (s := input()) != '':
    spisok = s.split()
    spisok = sorted(spisok)
    first = spisok[0]    # герой
    friend = spisok[1]    # друг 1-го уровня
           
    if first not in names:    # если героя нет в словаре друзей, то
        names[first] = []    # создаем список ключ=герой, значение
    names[first].append(friend)    # в словарь добавляем ключ=герой, значение=друг 1-го уровня
    if friend not in names:    # если друга 1-го уровня нет в словаре, то
        names[friend] = []    # создаем список ключ=друг, значение
    names[friend].append(first)    # в словарь добавляем ключ=друг, значение=герой 

friends_names = {}    # создаем словарь для друзей 2-го уровня

for name in names:    # для каждого героя в таблице с друзьями 1-го уровня
    friends = set(names[name])    # множество друзей 1-го уровня
    second = set()    # множество друзей 2-го уровня
    
    for friend in friends:    # для каждого друга из списка друзей 1-го уровня
        second.update(names[friend])    # добавляем во множество друзей 2-го уровня
    
    second -= friends    # убираем друзей 1-го уровня
    second -= {name}    # убираем самого себя

    friends_names[name] = sorted(second)
for name in sorted(friends_names):
    print(f'{name}: {", ".join(friends_names[name])}')

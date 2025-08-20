def grow(*position, **kwargs):
    names = list(kwargs.keys())    # создаем словрь именных
    ans = []    # список для финалки
    for number in position:
        updated = False    # флаг для обработанных чисел в позиционных
        suma = 0    # тут будет финальная "надбавка" после обработки всех именных
        for name in names:    # для каждого ключа словаря именных
            if number % len(name) == 0:    # если позиц.число кратно значению именного
                suma += kwargs[name]    # добавляем значение этого именного в общую сумму "надбавки"
                updated = True    # чтобы мы знали, что число обработано и мы его больше не трогаем
        if updated:
            ans.append(number + suma)    # добавляем к нашему позиц.число "набавку" и в фин.список
        else:
            ans.append(number)    # если число никак не обработано, то добавляем его в фин.список
    return tuple(ans)
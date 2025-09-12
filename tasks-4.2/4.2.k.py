def order(*args):
    coffee_dict = {
        'Эспрессо': {'coffee': 1},
        'Капучино': {'coffee': 1, 'milk': 3},
        'Макиато': {'coffee': 2, 'milk': 1},
        'Кофе по-венски': {'coffee': 1, 'cream': 2},
        'Латте Макиато': {'coffee': 1, 'milk': 2, 'cream': 1},
        'Кон Панна': {'coffee': 1, 'cream': 1},
    }
    ans = []
    for beverage in args:
        reciepe = coffee_dict.get(beverage)    # словарь рецептов
        enough = True    # флаг, что всего хватает
        for ingredient, amount in reciepe.items():
            if in_stock.get(ingredient) < amount:    # со склада берем по ключу количество
                enough = False    # если на складе меньше требуемого, то флаг фолс
                break

        if not enough:
            continue
        for ingredient, amount in reciepe.items():
            in_stock[ingredient] -= amount    # отнимаем со склада использованное количество ингредиентов
        ans.append(beverage)
        break    # приготовили один напиток - и конец
    if ans == []:
        return 'К сожалению, не можем предложить Вам напиток'
    else:
        return (' '.join(ans))
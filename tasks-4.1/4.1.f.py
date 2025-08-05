def move(player, number):
    global count, result
    if player == 'Петя':
        count += number
    elif player == 'Ваня':
        count -= number
    if count > 0:
        result = 'Петя'
    elif count < 0:
        result = 'Ваня'
    else:
        result = 'Ничья'


def game_over():
    return result


result = ''
count = 0
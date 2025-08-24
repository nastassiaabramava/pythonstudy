def login(username, password, success, error):
    suma = hex((sum(ord(i) for i in username)) * len(username))    # вычисляем правильный пароль
    result = suma[2:][::-1].upper()    # срез с 2: потому что в хексе обязательный 0х
    if result == password.upper():
        return success(username)
    else:
        return error(username)
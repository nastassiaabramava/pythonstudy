import json
file_1 = input()
file_2 = input()

with open(file_1, encoding='utf-8') as file_in, \
        open(file_2, encoding='utf-8') as file_change:
    users = json.load(file_in)
    updates = json.load(file_change)

slov = {}
for line in users:
    if 'name' in line:
        new_key = line['name']    # имя пользователя становится ключом
        new_value = {key: value for key, value in line.items() if key != 'name'}
        slov[new_key] = new_value    # новым значением становится словарь из объектов

for line in updates:
    name = line['name']
    update_value = {key: value for key, value in line.items() if key != 'name'}    
    # измененные значения по юзерам без имени

    # если имя есть в исходном файле, то сравниваем значения обоих файлов
    if name in slov:
        for key, value in update_value.items():
            old_value = slov[name].get(key, '')    
            # берем старое значение, если есть иначе возвращаем пустую строку
            slov[name][key] = max(old_value, value)    
            # значение ключа, который является значение ключа более высокого уолвня
        # если такого имени нет, то добавляем
    else:
        slov[name] = update_value

with open(file_1, 'w', encoding='utf-8') as file_out:
    json.dump(slov, file_out, ensure_ascii=False, indent=4)

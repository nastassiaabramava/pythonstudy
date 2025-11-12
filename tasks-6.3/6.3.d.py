from requests import get


address = input()
key = input()
response = get(f'http://{address}/').json()    #ответ в формате словаря
print(response.get(key, "No data"))    #получаем значение по ключу или no data
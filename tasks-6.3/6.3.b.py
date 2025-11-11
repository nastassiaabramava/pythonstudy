from requests import get


address = input()
result = 0
while True:
    response = get(f'http://{address}/')
    x = int(response.text)    #берем текст ответа и преобразовываем его в инт
    if x == 0:
        break
    result += x
print(result)
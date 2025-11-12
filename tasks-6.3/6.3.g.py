from requests import get
import sys


address = input().strip()
user_id = int(input().strip())
# берем ид юзера
users = get(f'http://{address}/users/{user_id}')
# и проверяем его статус
if users.status_code != 200:
    print('Пользователь не найден')
    sys.exit(0)
# словарик из джейсона
user = users.json()
# читаем, что там дальше на вводе
message = sys.stdin.read()
# форматируем, чтобы подставить инфу из словаря
message = message.format(**user)
print(message)
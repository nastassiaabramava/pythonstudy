from requests import put
import sys


address, user_id, *data = map(str.strip, sys.stdin)
# с помощью лямбды разделяем все строки по =
# делаем словарь из получившихся пар
user = {key: value for key, value in map(lambda x: x.split('='), data)}
put(f'http://{address}/users/{user_id}', json=user)
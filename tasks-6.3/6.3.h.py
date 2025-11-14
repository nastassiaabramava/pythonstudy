from requests import post
import sys


address, *data = map(str.strip, sys.stdin)
user = dict(zip(('username', 'last_name', 'first_name', 'email'), data))
post(f'http://{address}/users/', json=user)
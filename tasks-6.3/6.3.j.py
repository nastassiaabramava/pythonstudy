from requests import delete
import sys


address, user_id = map(str.strip, sys.stdin)
delete(f'http://{address}/users/{user_id}')
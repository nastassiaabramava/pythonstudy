from requests import get


address = input().strip()
users = get(f'http://{address}/users').json()
full_names = [f"{user['last_name']} {user['first_name']}" for user in users]
for user in sorted(full_names):
    print(user)
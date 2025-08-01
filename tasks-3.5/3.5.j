with open(input(), encoding="utf-8") as file_in:
    lines = file_in.readlines()
n = int(input())
last_lines = lines[-n:]
for line in last_lines:
    print(line.rstrip())

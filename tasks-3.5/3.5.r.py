import math
filename = input()

with open(filename, 'rb') as file_in:
    file_in.seek(0, 2)
    size = file_in.tell()
if size < 1024:
    print(size, 'Б', sep='')
elif size < 1024 * 1024:
    print(math.ceil(size / 1024), 'КБ', sep='')
elif size < 1024 * 1024 * 1024:
    print(math.ceil(size / (1024 * 1024)), 'МБ', sep='')
else:
    print(math.ceil(size / (1024 * 1024 * 1024)), 'ГБ', sep='')

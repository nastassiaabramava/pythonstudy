n = int(input())
prev = 0
bad = -1

for i in range(n):
    block = int(input())
    h = block % 256
    r = (block // 256) % 256
    m = block // (256 * 256)
    hash = (37 * (m + r + prev)) % 256
    if bad == -1 and (h >= 100 or h != hash):
        bad = i
    prev = h
print(bad)
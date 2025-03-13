from collections import deque
import sys
s, t = map(int, input().split())

if s == t:
    print("0")
    sys.exit()

d = deque()
d.append([s, ""])
visited = set()
res = -1
while d:
    cur, record = d.popleft()
    if cur == t:
        res = record
        break

    if 0 <= cur * cur <= 10 ** 9 and cur * cur not in visited:
        visited.add(cur * cur)
        d.append([cur * cur, record + "*"])
    if 0 <= cur + cur <= 10 ** 9 and cur + cur not in visited:
        visited.add(cur + cur)
        d.append([cur + cur, record + "+"])
    if 0 not in visited:
        visited.add(0)
        d.append([0, record + "-"])
    if cur > 0 and 1 not in visited:
        visited.add(1)
        d.append([1, record + "/"])
print(res)
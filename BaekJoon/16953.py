from collections import deque

n, m = map(int, input().split())
v = set()
q = deque()

q.append([n, 1])
minn = 10 ** 9
while q:
    cur, time = q.popleft()
    if cur == m:
        minn = min(minn, time)

    for dx in [cur, cur * 9 + 1]:
        nx = dx + cur
        if 0 <= nx <= 10**9 and nx not in v:
            v.add(nx)
            q.append([nx, time + 1])

if minn == 10 ** 9:
    print(-1)
else:
    print(minn)
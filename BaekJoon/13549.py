from collections import deque

n, k = map(int, input().split())
v = set()
q = deque()
q.append([n, 0])
mint = 10 ** 6
while q:
    cur, time = q.popleft()
    if cur == k:
        mint = min(mint, time)
    for dx, dt in [[cur, 0], [-1, 1], [1, 1]]:
        ncur = dx + cur
        if 0 <= ncur <= 100000 and ncur not in v:
            v.add(ncur)
            q.append([ncur, time + dt])
print(mint)


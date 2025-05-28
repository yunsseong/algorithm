import sys
from collections import deque

n, k = map(int, input().split())
q = deque()
q.append([n, str(n)])
visited = [False] * 100001
dist = [0] * 100001

if n > k:
    print(n - k)
    print(*[i for i in range(n, k - 1, -1)])
    sys.exit()

while q:
    c, t = q.popleft()
    if c == k:
        print(dist[k])
        print(t)
        break
    for d in [-1, 1, c]:
        nc = c + d
        if 0 <= nc <= 100000 and not visited[nc]:
            visited[nc] = True
            dist[nc] = dist[c] + 1
            q.append([nc, t + " " + str(nc)])
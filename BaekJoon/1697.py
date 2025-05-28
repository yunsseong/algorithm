from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)
visited = [False] * 100001
dist = [0] * 100001
while q:
    c = q.popleft()
    if c == k:
        print(dist[k])
        break
    for d in [-1, 1, c]:
        nc = c + d
        if 0 <= nc <= 100000 and not visited[nc]:
            visited[nc] = True
            dist[nc] = dist[c] + 1
            q.append(nc)

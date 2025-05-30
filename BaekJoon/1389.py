from collections import deque
n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
g = [[] for i in range(n + 1)]
for s, e in ls:
    g[s].append(e)
    g[e].append(s)
res = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: continue
        visited = [False] * (n + 1)
        visited[i] = True
        q = deque()
        q.append((i, 0))
        while q:
            c, cnt = q.popleft()
            if c == j:
                res[i] += cnt
                break
            for nc in g[c]:
                if not visited[nc]:
                    visited[nc] = True
                    q.append((nc, cnt + 1))
print(res.index(min(res[1:])))

from collections import deque

n, m, k = map(int, input().split())
b = [list(input()) for _ in range(n)]
q = deque()
visited = []
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append([False] * (k + 1))
    visited.append(tmp)

q.append([0, 0, 1, 0])
res = -1
while q:
    r, c, cnt, kcnt = q.popleft()
    if kcnt > k:
        continue
    if r == n - 1 and c == m - 1:
        res = cnt
        break
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and 0 <= kcnt <= k and not visited[nr][nc][kcnt]:
            visited[nr][nc][kcnt] = True
            if b[nr][nc] == "1":
                q.append([nr, nc, cnt + 1, kcnt + 1])
            else:
                q.append([nr, nc, cnt + 1, kcnt])
print(res)
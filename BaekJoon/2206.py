# 9:10
from collections import deque
n, m = map(int, input().split())
ls = [list(input()) for _ in range(n)]
res = 1e9
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = True
q = deque()
q.append((0, 0, 1, 0))
while q:
    r, c, cnt, wall = q.popleft()
    if r == n - 1 and c == m - 1:
        res = min(res, cnt)
        break
    for dr, dc in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc][wall]:
            if ls[nr][nc] == "0":
                visited[nr][nc][wall] = True
                q.append((nr, nc, cnt + 1, wall))

            if ls[nr][nc] == "1" and wall == 0:
                visited[nr][nc][wall + 1] = True
                q.append((nr, nc, cnt + 1, wall + 1))
print(res if res != 1e9 else -1)

import sys
from collections import deque
col, row = map(int, input().split())
visited = [[False] * col for _ in range(row)]
dist = [[0] * col for _ in range(row)]
ls = []
q = deque()
t = 0
f = 0
for i in range(row):
    tmp = list(map(int, input().split()))
    for j, x in enumerate(tmp):
        if x == -1:
            f += 1
            continue
        if x == 1:
            t += 1
            visited[i][j] = True
            q.append([i, j])
    ls.append(tmp)

if t + f == col * row:
    print(0)
    sys.exit()

while q:
    r, c = q.popleft()
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < row and 0 <= nc < col and ls[nr][nc] != -1 and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append([nr, nc])
            dist[nr][nc] = dist[r][c] + 1

if sum(map(sum, visited)) + f != row * col:
    print(-1)
else:
    print(max(map(max, dist)))





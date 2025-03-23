from collections import deque

n, m = map(int, input().split())
b = []
d = []
q = deque()
visited = [[-1] * m for _ in range(n)]
wall = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 2:
            d = [i, j, 0]
        if row[j] == 0:
            wall.append([i, j])
    b.append(row)
q.append(d)
visited[d[0]][d[1]] = 0

for i, j in wall:
    visited[i][j] = 0

while q:
    cr, cc, cnt = q.popleft()
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr, nc = cr + dr, cc + dc

        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 and b[nr][nc] == 1:
            visited[nr][nc] = cnt + 1
            q.append([nr, nc, cnt + 1])

for i in visited:
    print(*i)



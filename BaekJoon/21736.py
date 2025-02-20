from collections import deque

n, m = map(int, input().split())
c = [list(input()) for _ in range(n)]
v = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if c[i][j] == "I":
            d = deque([(i, j)])

while d:
    x, y = d.popleft()
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and c[nx][ny] != "X":
            v[nx][ny] = True
            if c[nx][ny] == "P":
                cnt += 1
            d.append([nx, ny])

print("TT" if cnt == 0 else cnt)


from collections import deque

n, m = map(int, input().split())
ls = [list(input()) for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if ls[i][j] == "L":
            q = deque()
            visited = [[False] * m for _ in range(n)]
            visited[i][j] = True
            q.append([i, j, 0])
            while q:
                r, c, cnt = q.popleft()
                res = max(res, cnt)
                for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and ls[nr][nc] == "L" and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append([nr, nc, cnt + 1])
print(res)
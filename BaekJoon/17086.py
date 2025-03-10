from collections import deque
n, m = map(int, input().split())
b = [input().split() for _ in range(n)]
count = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        d = deque()
        d.append([i, j, 0])
        visited = [[False] * m for _ in range(n)]
        visited[i][j] = True
        while d:
            r, c, cnt = d.popleft()
            if b[r][c] == "1":
                count[i][j] = cnt
                break

            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    visited[nr][nc] = True
                    d.append([nr, nc, cnt + 1])
print(max(map(max, count)))
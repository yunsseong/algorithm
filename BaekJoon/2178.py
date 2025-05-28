from collections import deque

n, m = map(int, input().split())
ls = [list(input()) for _ in range(n)]
q = deque()
visited = [[False] * m for _ in range(n)]
dist = [[1] * m for _ in range(n)]
q.append([0, 0])
while q:
    r, c = q.popleft()
    if r == n - 1 and c == m - 1:
        print(dist[n-1][m-1])
        break
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and ls[nr][nc] == "1" and not visited[nr][nc]:
            visited[nr][nc] = True
            dist[nr][nc] = dist[r][c] + 1
            q.append([nr, nc])
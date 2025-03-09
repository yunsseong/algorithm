from collections import deque

m, n = map(int, input().split())
b = [list(input()) for _ in range(n)]
d = deque()
d.append([0, 0, 0])
visited = [[False] * m for _ in range(n)]
while d:
    r, c, w = d.popleft()
    if r == n - 1 and c == m - 1:
        print(w)
        break
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = True
            if b[nr][nc] == "1":
                d.append([nr, nc, w + 1])
            else:
                d.appendleft([nr, nc, w])
from collections import deque
m, n = map(int, input().split())
b = [list(input()) for _ in range(n)]
q = deque()
visited = [[False] * m for _ in range(n)]
score = {"W":0, "B":0}

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            q.append([i, j])
            cnt = 0
            cur = b[i][j]
            while q:
                r, c = q.popleft()
                for dr, dc in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr and nr < n and 0 <= nc and nc < m and not visited[nr][nc] and cur == b[nr][nc]:
                        visited[nr][nc] = True
                        q.append([nr, nc])
                        cnt += 1
            if cnt == 0: cnt += 1
            score[cur] += cnt ** 2

print(score["W"], score["B"])




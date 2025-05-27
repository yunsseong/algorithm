n = int(input())
ls = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 0
res = []
def dfs(r, c):
    global house
    for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and ls[nr][nc] == "1" and not visited[nr][nc]:
            visited[nr][nc] = True
            house += 1
            dfs(nr, nc)

for i in range(n):
    for j in range(n):
        if ls[i][j] == "1" and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            house = 1
            dfs(i, j)
            res.append(house)

print(cnt)
print(*sorted(res), sep = "\n")

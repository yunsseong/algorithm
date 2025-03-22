from collections import deque

# 17:01

# 한수 왼쪽 아래점에 있고, 집은 오른쪽 위
# T는 방문이 안되는 곳

r, c, k = map(int, input().split())
b = [list(input()) for _ in range(r)]
q = deque()
q.append([r - 1, 0, [[r-1, 0]]])
p = 0

while q:
    cr, cc, visited = q.popleft()
    if len(visited) == k:
        if cr == 0 and cc == (c - 1):
            p += 1
        continue
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < r and 0 <= nc < c and [nr, nc] not in visited and b[nr][nc] != "T":
            q.append([nr, nc, visited + [[nr, nc]]])
print(p)




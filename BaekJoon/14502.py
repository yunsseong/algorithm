from itertools import combinations
from collections import deque

n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
area = n * m
cord = []
s = []
wall_cnt = 0
res = 0
for i in range(n):
    for j in range(m):
        cord.append([i, j])
        if b[i][j] == 2:
            s.append([i, j])
        if b[i][j] == 1:
            wall_cnt += 1
wall_cnt += 3
combs = list(combinations(cord, 3))

for comb in combs:
    d = deque()
    unsafe_area = 0
    visited = [[False] * m for _ in range(n)]
    for r, c in s:
        if not visited[r][c]:
            unsafe_area += 1
            visited[r][c] = True
            d.append([r, c])

            while d:
                cr, cc = d.popleft()
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and [nr, nc] not in comb and b[nr][nc] != 1:
                        visited[nr][nc] = True
                        unsafe_area += 1
                        d.append([nr, nc])
    safe_area = area - unsafe_area - wall_cnt
    res = max(res, safe_area)
print(res)
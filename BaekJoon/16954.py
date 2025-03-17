import sys
from collections import deque
import copy
tmp = deque()
tmp.extend([list(input()) for _ in range(8)])
b = []
for _ in range(8):
    b.append(copy.deepcopy(tmp))
    tmp.pop()
    tmp.appendleft(["."] * 8)
q = deque()
q.append([7, 0, 0])
visited = [[[False] * 16 for _ in range(8)] for _ in range(8)]
while q:
    r, c, cnt = q.popleft()
    idx = cnt
    if idx >= 8:
        idx = 7
    if b[idx][r][c] == "#":
        continue
    if r == 0 and c == 7:
        print(1)
        sys.exit()
    for dr, dc in [[-1, 0], [0, -1], [0, 1], [1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1], [0, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 8 and 0 <= nc < 8 and not visited[nr][nc][cnt]:
            visited[nr][nc][cnt] = True
            if b[idx][nr][nc] == ".":
                q.append([nr, nc, cnt + 1])
print(0)
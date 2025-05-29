import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    e = list(map(int, input().split()))
    v = [[False] * n for _ in range(n)]
    q = deque()
    q.append((*s, 0))
    v[s[0]][s[1]] = True
    while q:
        r, c, cnt = q.popleft()
        if [r, c] == e:
            print(cnt)
            break
        for dr, dc in [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not v[nr][nc]:
                v[nr][nc] = True
                q.append((nr, nc, cnt + 1))


from collections import deque

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    b = [list(map(int, input().split())) for _ in range(h)]
    d = deque()
    v = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not v[i][j] and b[i][j] == 1:
                v[i][j] = True
                d.append([i, j])

                while d:
                    r, c = d.popleft()

                    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < h and 0 <= nc < w and not v[nr][nc] and b[nr][nc] == 1:
                            v[nr][nc] = True
                            d.append([nr, nc])
                cnt += 1
    print(cnt)


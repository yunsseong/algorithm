from collections import deque

n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
q = deque([(0, 0, n)])
bcnt, wcnt = 0, 0
while q:
    r, c, l = q.popleft()

    blue = True
    white = True
    for i in range(r, r + l):
        for j in range(c, c + l):
            if b[i][j] == 0:
                blue = False
            else:
                white = False

    if not white and not blue:
        q.extend([[r, c, l // 2], [r, c + l // 2, l // 2], [r + l // 2, c, l // 2], [r + l // 2, c + l // 2, l // 2]])
        continue

    if blue:
        bcnt += 1
    if white:
        wcnt += 1

print(wcnt, bcnt)
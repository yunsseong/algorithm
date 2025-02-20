from collections import deque

n = int(input())
rgb = []
sb = []

for _ in range(n):
    row = list(input())
    rgb_tmp = []
    sb_tmp = []
    for e in row:
        if e == "B":
            sb_tmp.append(e)
        else:
            sb_tmp.append("S")
        rgb_tmp.append(e)
    rgb.append(rgb_tmp)
    sb.append(sb_tmp)

def cal(board):
    cnt = 0
    v = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not v[i][j]:
                cur_color = board[i][j]
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy  in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not v[nx][ny] and board[nx][ny] == cur_color:
                            v[nx][ny] = True
                            q.append([nx, ny])

                cnt += 1
    return cnt

print(cal(rgb), cal(sb))
from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for x in range(n):
    c = [0 for _ in range(n)]
    q = deque()
    q.append(x)

    while q:
        cur = q.popleft()

        for i in range(n):
            if g[cur][i] == 1 and c[i] == 0:
                c[i] = 1
                visited[x][i] = 1
                q.append(i)

for x in range(n):
    print(*visited[x], sep = " ")

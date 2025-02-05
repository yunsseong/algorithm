from collections import deque

n, m = map(int, input().split())
board, count = [[] for _ in range(101)], [0 for _ in range(101)]
visited = [False] * 101
q = deque()
q.append(1)

for _ in range(n+m):
    x, y = map(int, input().split())
    board[x].append(y)

while q:
    cur = q.popleft()
    if cur == 100:
        print(count[cur])
        break

    for i in range(1, 7):
        next = cur + i

        if next <= 100 and not visited[next]:
            if len(board[next]) == 1:
                next = board[next][0]
            if not visited[next]:
                visited[next] = True
                count[next] = count[cur] + 1
                q.append(next)
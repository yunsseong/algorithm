n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

stack = []
stack.append(1)
visited = [False for _ in range(n+1)]

cnt = 0
for i in range(1, n+1):
    stack.append(i)
    if visited[i]:
        continue
    while stack:
        cur = stack.pop()
        visited[cur] = True
        for next in g[cur]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)
    cnt += 1
print(cnt)
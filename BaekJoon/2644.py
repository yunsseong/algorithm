n = int(input())
x, y = map(int, input().split())
m = int(input())
ls = [list(map(int, input().split())) for _ in range(m)]
g = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = 1e9
def dfs(cur, cnt):
    global res
    if cur == y:
        res = min(res, cnt)
    for i in g[cur]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False

for s, e in ls:
    g[s].append(e)
    g[e].append(s)

visited[x] = True
dfs(x, 0)
if res == 1e9:
    print(-1)
else:
    print(res)



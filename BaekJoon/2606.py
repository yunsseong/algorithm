def dfs(cur):
    visited[cur] = True
    for i in g[cur]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

n = int(input())
m = int(input())
ls = [list(map(int, input().split())) for _ in range(m)]
g = [[] for _ in range(n + 1)]
for s, e in ls:
    g[s].append(e)
    g[e].append(s)
visited = [False] * (n + 1)
dfs(1)
print(sum(visited) - 1)






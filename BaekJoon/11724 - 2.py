import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

def dfs(cur):
    for i in g[cur]:
        if not v[i]:
            v[i] = True
            dfs(i)

n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
g = [[] for _ in range(n + 1)]
v = [False] * (n + 1)
for s, e in ls:
    g[s].append(e)
    g[e].append(s)

cnt = 0
for i in range(1, n + 1):
    if not v[i]:
        v[i] = True
        cnt += 1
        dfs(i)
print(cnt)




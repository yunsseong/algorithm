import sys
sys.setrecursionlimit(10**9)

n = int(input())
d = {i: [] for i in range(1, n+1)}

for _ in range(n-1):
    a, b = list(map(int, input().split()))
    d[a].append(b)
    d[b].append(a)

parents = [0] * (n+1)

def dfs(cur):
    for i in d[cur]:
        if parents[i] == 0:
            parents[i] = cur
            dfs(i)

dfs(1)
print(*parents[2:], sep="\n")
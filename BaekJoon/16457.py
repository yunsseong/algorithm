import sys

n, m, k = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]

def rec(select, cur, start):
    global ls, selected, visited
    if cur == select:
        slist = sum(selected, [])
        if len(set(slist)) <= n:
            print(select)
            sys.exit()
        return

    for i in range(start, m):
        if visited[i]:
            continue

        visited[i] = True
        selected[cur] = ls[i]
        rec(select, cur + 1, i + 1)
        visited[i] = False

for k in range(m, -1, -1):
    selected = [[] for i in range(k)]
    visited = [False] * m
    rec(k, 0, 0)
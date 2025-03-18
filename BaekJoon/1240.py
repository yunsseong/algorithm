n, m = map(int, input().split())
t = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    t[a].append([b, d])
    t[b].append([a, d])

def rec(node, distance):
    global visited, res
    if node == destination:
        res = distance
        return

    for nxt, d in t[node]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        rec(nxt, distance + d)

for _ in range(m):
    start, destination = map(int, input().split())
    visited = [False] * (n+1)
    visited[start] = True
    res = 1000 * 10000
    rec(start, 0)
    print(res)
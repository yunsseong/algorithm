n, k = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
maxn = int(-1e9)

selected = [0] * k
visited = [False] * n
def rec(cur, start):
    global n, maxn
    if cur == k:
        taste = 0
        for i in range(k):
            for j in range(i, k):
                if i == j:
                    continue
                taste += ls[selected[i]][selected[j]]
        maxn = max(maxn, taste)
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        selected[cur] = i
        rec(cur + 1, i + 1)
        visited[i] = False
rec(0, 0)
print(maxn)
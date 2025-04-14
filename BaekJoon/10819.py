n = int(input())
ls = list(map(int, input().split()))
maxn = int(-1e9)
visited = [False] * n
selected = [0] * n
def rec(cur):
    global n, maxn
    if cur == n:
        s = 0
        for i in range(n - 1):
            s += abs(selected[i] - selected[i + 1])
        maxn = max(maxn, s)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        selected[cur] = ls[i]
        rec(cur + 1)
        visited[i] = False

rec(0)
print(maxn)
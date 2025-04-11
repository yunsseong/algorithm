n, m = map(int, input().split())
selected = [0] * m
def rec(cur, start):
    if cur == m:
        print(*selected)
        return

    for i in range(start, n):
        selected[cur] = i + 1
        rec(cur + 1, i)
rec(0, 0)

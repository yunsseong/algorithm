def rec(idx, money):
    global n, maxn
    if idx == n:
        maxn = max(maxn, money)
        return

    if idx > n:
        return

    rec(idx + ls[idx][0], money + ls[idx][1])
    rec(idx + 1, money)

n = int(input())
ls = []
maxn = 0
for _ in range(n):
    ls.append(list(map(int, input().split())))

rec(0, 0)
print(maxn)
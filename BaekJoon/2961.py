def rec(idx, sin, ssen, cnt):
    global n, ls, res
    if idx == n:
        if cnt != 0:
            res = min(res, abs(sin - ssen))
        return
    rec(idx + 1, sin * ls[idx][0], ssen + ls[idx][1], cnt + 1)
    rec(idx + 1, sin, ssen, cnt)

res = int(1e9)
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
rec(0, 1, 0, 0)
print(res)
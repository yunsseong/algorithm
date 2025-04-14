n, l, r, x = map(int, input().split())
ls = list(map(int, input().split()))
res = 0
def rec(idx, sum_level, min_level, max_level, cnt):
    global n, l, r, x, res
    if idx == n:
        if cnt >= 2 and l <= sum_level <= r and max_level - min_level >= x:
            res += 1
        return
    rec(idx + 1, sum_level + ls[idx], min(min_level, ls[idx]), max(max_level, ls[idx]), cnt + 1)
    rec(idx + 1, sum_level, min_level, max_level, cnt)
rec(0, 0, int(1e9), int(-1e9), 0)
print(res)

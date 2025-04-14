n, s = map(int, input().split())
ls = list(map(int, input().split()))
res = 0
def rec(idx, val, cnt):
    global res
    if idx == n:
        if val == s and cnt != 0:
            res += 1
        return
    rec(idx + 1, val + ls[idx], cnt + 1)
    rec(idx + 1, val, cnt)
rec(0, 0, 0)
print(res)
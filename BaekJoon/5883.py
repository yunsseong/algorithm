n = int(input())
e = [int(input()) for _ in range(n)]
se = set(e)
res = 0
for i in se:
    cnt = 0
    prv = 0
    for j in e:
        if i == j:
            continue
        if prv == j:
            cnt += 1
        else:
            prv = j
            res = max(res, cnt)
            cnt = 1
    res = max(res, cnt)
print(res)
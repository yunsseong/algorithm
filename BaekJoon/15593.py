n = int(input())
e = [list(map(int, input().split())) for _ in range(n)]
e.sort()

maxn = 0
for i in range(n):
    s = 0
    prv = 0
    for j in range(n):
        if i == j:
            continue
        s += e[j][1] - e[j][0]
        if prv > e[j][0]:
            s -= prv - e[j][0]
        prv = e[j][1]
    maxn = max(maxn, s)
print(maxn)

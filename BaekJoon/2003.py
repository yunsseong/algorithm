n, m = map(int, input().split())
ls = list(map(int, input().split()))
s, e = 0, 0
acc = ls[0]
cnt = 0
while e < n:
    if acc == m:
        cnt += 1
        e += 1
        if e < n:
            acc += ls[e]
        acc -= ls[s]
        s += 1
    elif acc < m:
        e += 1
        if e < n:
            acc += ls[e]
    elif acc > m:
        acc -= ls[s]
        s += 1
print(cnt)

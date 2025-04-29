n, m = map(int, input().split())
ls = [0] + list(map(int, input().split()))
q = [list(map(int, input().split())) for _ in range(m)]
ps = [0] * (n + 1)
for i in range(1, n + 1):
    ps[i] = ps[i - 1] + ls[i]

for i, j in q:
    print(ps[j] - ps[i - 1])


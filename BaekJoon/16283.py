a, b, n, w = map(int, input().split())
res = []
for i in range(1, n):
    if a * i + b * (n - i) == w:
        res.append([i, n - i])

if len(res) >= 2 or len(res) == 0:
    print(-1)
else:
    print(*res[0])

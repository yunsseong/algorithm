n = int(input())
x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

sol = [2500000000] * n
for i in x:
    for j in y:
        distance = []
        for cx, cy in zip(x, y):
            distance.append(abs(cx - i) + abs(cy - j))
        distance.sort()
        k_sum = [sum(distance[:k]) for k in range(1, n + 1)]
        for l in range(n):
            sol[l] = min(sol[l], k_sum[l])
print(*sol)
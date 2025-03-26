n, m, k = map(int, input().split())
u = n + m
res = 0
for i in range(1, n):
    if i * 2 <= n and i <= m and u - i * 3 >= k:
        res += 1
print(res)
from itertools import product

n, k = map(int, input().split())
coms = []
for i in range(1, n+1):
    coms.extend(list(product([1, 2, 3], repeat = i)))
res = []

for c in coms:
    if sum(c) == n:
        res.append(c)
res.sort()

if len(res) >= k:
    print('+'.join(map(str, res[k-1])))
else:
    print(-1)
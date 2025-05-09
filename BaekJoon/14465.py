"""
1 2 3 4 5 6 7 8 9 10
X X O O X O O O X X
1 1 0 0 1 0 0 0 1 1

1 2 3 4 5 6 7 8 9 10
1 1 1 1 1 1 1 0 0 0

"""

n, k, b = map(int, input().split())
fix = [0] * n
for _ in range(b):
    fix[int(input()) - 1] = 1
s, e = 0, k - 1
acc = sum(fix[s:e+1])
res = 10e9
while e < n:
    res = min(res, acc)
    acc -= fix[s]
    s += 1
    e += 1
    if e < n:
        acc += fix[e]
print(res)
a, b = map(int, input().split())
res = []

for i in range(-1000, 1001):
    if i ** 2 + 2 * a * i + b == 0:
        res.append(i)
print(' '.join(map(str, res)))
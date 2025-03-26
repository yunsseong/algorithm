n = int(input())
res = []
for i in range(1, 500):
    for j in range(1, 500):
        if i ** 2 - j ** 2 == n:
            res.append([i, j])
print(len(res))

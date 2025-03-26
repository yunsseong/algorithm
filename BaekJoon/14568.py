n = int(input())
s = []
for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if i + j + k != n:
                continue
            if i - j < 2:
                continue
            if k % 2 != 0:
                continue
            s.append([i, j, k])
print(len(s))
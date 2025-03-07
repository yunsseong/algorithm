n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
side1 = 0
side2 = 0
side3 = n * m

for i in range(n):
    for j in range(m):
        if i == 0:
            side1 += d[i][j]
        else:
            if d[i][j] > d[i-1][j]:
                side1 += d[i][j] - d[i-1][j]

for i in range(n):
    for j in range(m):
        if j == 0:
            side2 += d[i][j]
        else:
            if d[i][j] > d[i][j-1]:
                side2 += d[i][j] - d[i][j-1]

print((side1 + side2 + side3) * 2)

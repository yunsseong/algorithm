n = int(input())
x = []
y = []

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

conv_x = x[(n - 1) // 2]
conv_y = y[(n - 1) // 2]

cnt = 0
for i, j in zip(x, y):
    cnt += abs(conv_x - i) + abs(conv_y - j)
print(cnt)
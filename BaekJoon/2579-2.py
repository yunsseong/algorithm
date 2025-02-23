import sys

n = int(input())
points = [int(input()) for _ in range(n)]
points.insert(0, 0)
dp = [0] * (n+1)

if n == 1:
    print(points[1])
    sys.exit()
if n == 2:
    print(points[1] + points[2])
    sys.exit()

dp[1], dp[2] = points[1], points[1] + points[2]

for i in range(3, n + 1):
    dp[i] = max(points[i] + points[i - 1] + dp[i - 3], points[i] + dp[i - 2])

print(dp[n])
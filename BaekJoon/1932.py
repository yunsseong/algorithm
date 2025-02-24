import sys

n = int(input())
t = [[0]]

for _ in range(n):
    tmp = [0]
    tmp.extend(list(map(int, input().split())))
    t.append(tmp)

dp = [[0] * (n+1) for _ in range(n+1)]

dp[1][1] = t[1][1]

if n == 1:
    print(dp[1][1])
    sys.exit()

dp[2][1] = dp[1][1] + t[2][1]
dp[2][2] = dp[1][1] + t[2][2]

if n == 2:
    print(max(dp[2]))
    sys.exit()

for i in range(3, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + t[i][j]
print(max(dp[n]))



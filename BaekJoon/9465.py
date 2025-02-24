n = int(input())
for _ in range(n):
    m = int(input())
    points = [list(map(int, input().split())) for _ in range(2)]
    points[0].insert(0, 0)
    points[1].insert(0, 0)
    dp = [[0] * (m + 1) for _ in range(2)]
    dp[0][1] = points[0][1]
    dp[1][1] = points[1][1]
    if m == 1:
        print(max(dp[0][1], dp[1][1]))
        continue
    dp[0][2] = dp[1][1] + points[0][2]
    dp[1][2] = dp[0][1] + points[1][2]
    if m == 2:
        print(max(dp[0][2], dp[1][2]))
        continue
    for i in range(3, m + 1):
        dp[0][i] = max(dp[1][i-1] + points[0][i], max(dp[0][i-2], dp[1][i-2]) + points[0][i])
        dp[1][i] = max(dp[0][i-1] + points[1][i], max(dp[1][i-2], dp[0][i-2]) + points[1][i])
    print(max(dp[0][m], dp[1][m]))
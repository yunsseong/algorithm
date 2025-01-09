def cal(n):
    global dp

    if n == 1:
        return 0

    if n == 2:
        return 1

    if n == 3:
        return 1

    dp[1], dp[2], dp[3] = 0, 1, 1

    for i in range(4, n + 1):
        if i % 6 == 0:
            dp[i] = min(min(dp[i//3], dp[i//2]), dp[i-1]) + 1
            continue

        if i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
            continue

        if i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
            continue

        dp[i] = dp[i-1] + 1
    return dp[n]


n = int(input())
dp = [0] * (n + 1)
print(cal(n))

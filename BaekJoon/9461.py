n = int(input())
dp = [0] * (101)
dp[1] = 1
dp[2] = 1
dp[3] = 1
for _ in range(n):
    case = int(input())
    if case <= 3:
        print(1)
        continue
    for i in range(4, case+1):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[case])




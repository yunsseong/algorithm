from collections import deque

n = int(input())
b = deque()
b.append(list(map(int, (input().split()))))
max_dp = deque()
min_dp = deque()

max_dp.append([0, b[0][0], b[0][1], b[0][2], 0])
max_dp.append([0] * 5)

min_dp.append([900000, b[0][0], b[0][1], b[0][2], 900000])
min_dp.append([900000] * 5)
b.popleft()

for _ in range(n - 1):
    b.append(list(map(int, (input().split()))))
    for i in range(1, 4):
        max_dp[1][i] = max(max_dp[0][i], max_dp[0][i + 1], max_dp[0][i - 1]) + b[0][i - 1]
        min_dp[1][i] = min(min_dp[0][i], min_dp[0][i + 1], min_dp[0][i - 1]) + b[0][i - 1]
    b.popleft()

    max_dp.popleft()
    min_dp.popleft()
    max_dp.append([0] * 5)
    min_dp.append([900000] * 5)

print(max(max_dp[0]), min(min_dp[0]))
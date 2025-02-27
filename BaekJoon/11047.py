n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
while k != 0:
    for i in range(n):
        if coins[i] > k:
            cnt += k // coins[i-1]
            k = k % coins[i-1]
            break

        if i == n-1:
            cnt += k // coins[i]
            k = k % coins[i]
print(cnt)
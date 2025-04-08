import math

n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    res = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            res = max(res, math.gcd(nums[i], nums[j]))
    print(res)
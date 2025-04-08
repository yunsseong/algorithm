n = int(input())
nums = list(map(int, input().split()))
res = 0
for i in nums:
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
           cnt += 1
    if cnt == 2:
       res += 1
print(res)
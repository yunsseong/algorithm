from itertools import product
n = int(input())
nums = list(product(["0", "1", "2"], repeat = n))
cnt = 0
for num in nums:
    if num[0] != "0":
        if int(''.join(num)) % 3 == 0:
            cnt += 1

print(cnt)
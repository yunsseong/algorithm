from collections import defaultdict

n = int(input())
num = [int(input()) for _ in range(n)]
dict = defaultdict(int)
num.sort()

for i in num:
    dict[i] += 1

maxn = max(dict.values())
find_max = [i for i, j in dict.items() if j == maxn]

print(round(sum(num) / len(num)))
print(num[len(num) // 2])
if len(find_max) >= 2:
    print(find_max[1])
else:
    print(find_max[0])
print(max(num) - min(num))
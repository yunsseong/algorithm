from collections import defaultdict

n = int(input())
tang = list(map(int, input().split()))
counter = defaultdict(int)
left = 0
right = 0
maxn = 0
counter[tang[left]] += 1

while left <= right and left < len(tang) and right < len(tang):
    if len(counter) <= 2:
        maxn = max(maxn, right - left + 1)
        right += 1
        if right < len(tang):
            counter[tang[right]] += 1
    else:
        counter[tang[left]] -= 1
        if counter[tang[left]] == 0:
            del counter[tang[left]]
        left += 1
print(maxn)
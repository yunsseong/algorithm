from itertools import permutations

n, k = map(int, input().split())
a = list(map(int, input().split()))
ps = list(permutations(a))
cnt = 0
for p in ps:
    cur = 500
    under = False
    for i in p:
        cur = cur + i - k
        if cur < 500:
            under = True
            break
    if not under:
        cnt += 1
print(cnt)

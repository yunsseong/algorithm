from itertools import permutations

def solution(k, dungeons):
    maxn = 0
    cases = list(permutations(dungeons))
    for case in cases:
        cur = k
        cnt = 0
        for dungeon in case:
            if cur >= dungeon[0]:
                cur -= dungeon[1]
                cnt += 1
        maxn = max(maxn, cnt)
    return maxn
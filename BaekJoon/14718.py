import sys
input = sys.stdin.readline

n, k = map(int, input().split())
force, agility, intelli, soldier = [], [], [], []

for _ in range(n):
    f, a, i = map(int, input().split())
    force.append(f)
    agility.append(a)
    intelli.append(i)
    soldier.append([f, a, i])

stat = 1000000 * 3
for f in force:
    for a in agility:
        for i in intelli:
            if stat < f + a + i:
                continue
            cnt = 0
            for sf, sa, si in soldier:
                if f >= sf and a >= sa and i >= si:
                    cnt += 1
            if cnt >= k:
                stat = min(stat, f + a + i)
print(stat)


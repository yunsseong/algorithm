import heapq

n, m = map(int, input().split())
table = []
pool = []

for _ in range(n):
    table.append(list(map(int, input().split())))

table.sort(reverse = True)
cnt = 0

while len(table) != 0:
    start, use = table.pop()

    if len(pool) == 0:
       heapq.heappush(pool, start + use)
       continue

    while len(pool) != 0 and pool[0] + m < start:
        heapq.heappop(pool)

    if len(pool) != 0 and pool[0] <= start:
        heapq.heappop(pool)
        cnt += 1
    heapq.heappush(pool, start + use)
print(cnt)
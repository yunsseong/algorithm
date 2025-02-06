from collections import deque

n, d = map(int, input().split())
counter = [10 ** 6 for i in range(d + 1)]
load = dict()

for _ in range(n):
    start, end, length = map(int, input().split())
    if start not in load:
        load[start] = []

    load[start].append([end, length])
    load[start].sort()

q = deque()
q.append(0)

min_n = 10 ** 9
counter[0] = 0

while q:
    cur = q.popleft()

    if cur == d:
        min_n = min(min_n, counter[d])

    if cur in load.keys():
        for end, length in load[cur]:
            if end <= d and length <= end - cur:
                q.append(end)
                counter[end] = min(counter[end], counter[cur] + length)

    if cur + 1 <= d:
        q.append(cur + 1)
        counter[cur + 1] = min(counter[cur + 1], counter[cur] + 1)

print(min_n)


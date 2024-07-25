n = int(input())
time = []
max_time = 0

for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[1], x[0]))
time_able = []
cnt = 0
max_cursor = 0
for start, end in time:
    if start >= max_cursor:
        max_cursor = end
        cnt += 1

print(cnt)
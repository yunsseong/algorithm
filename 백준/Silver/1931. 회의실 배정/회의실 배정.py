n = int(input())
time = []

for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[1], x[0]))
cnt = 0
cursor = 0
for start, end in time:
    if start >= cursor:
        cursor = end
        cnt += 1

print(cnt)
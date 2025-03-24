n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    count = 1
    for j in range(n):
        if i == j:
            continue
        if p[j][0] > p[i][0] and p[j][1] > p[i][1]:
            count += 1
    print(count)
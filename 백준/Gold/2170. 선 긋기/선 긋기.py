n = int(input())
line = []
for _ in range(n):
    line.append(list(map(int, input().split())))
line.sort()

end = -1000000000
res = 0
for i in range(len(line)):
    if line[i][0] >= end:
        res += line[i][1] - line[i][0]
        end = line[i][1]
    else:
        if line[i][1] > end:
            res += line[i][1] - end
            end = line[i][1]
print(res)
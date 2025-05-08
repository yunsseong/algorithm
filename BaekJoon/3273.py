n = int(input())
ls = sorted((map(int, input().split())))
x = int(input())
s, e = 0, n - 1
cnt = 0
while s < e:
    if ls[s] + ls[e] == x:
        cnt += 1
        e -= 1
        s += 1
    elif ls[s] + ls[e] > x:
        e -= 1
    elif ls[s] + ls[e] < x:
        s += 1
print(cnt)



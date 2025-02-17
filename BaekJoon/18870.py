n = int(input())
cord = list(map(int, input().split()))
s = sorted(set(cord))
d = {s[i]:i for i in range(len(s))}
for i in cord:
    print(d[i], end = " ")


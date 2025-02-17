n, m = map(int, input().split())
d1 = dict()
d2 = dict()
for i in range(n):
    name = input()
    d1[name] = i + 1
    d2[i + 1] = name

for _ in range(m):
    i = input()
    if i.isdigit():
        print(d2[int(i)])
    else:
        print(d1[i])
n = input()
take = sorted(list(map(int, input().split())))
accum = 0
res = 0
for i in take:
    accum += i
    res += accum
print(res)
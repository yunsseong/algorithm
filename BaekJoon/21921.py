n, x = map(int, input().split())
v = list(map(int, input().split()))

start = 0
end = x - 1
cum = sum(v[start:end + 1])
res = cum
cnt = 1
while True:
    start += 1
    end += 1

    cum = cum - v[start - 1] + v[end]
    if cum > res:
        res = cum
        cnt = 1
    elif cum == res:
        cnt += 1

    if end == n - 1:
        break
if res != 0:
    print(res)
    print(cnt)
else:
    print("SAD")

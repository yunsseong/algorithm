n, m = map(int, input().split())
ls = []
for _ in range(n):
    guitar, able = input().split()
    conv = ["1" if i == "Y" else "0" for i in list(able)]
    ls.append([guitar, int(('0b'+''.join(conv)), 2)])
res = []
def rec(idx, val, cnt):
    global res
    if idx == n:
        if cnt == 0 or val == 0:
            return
        res.append([val, cnt])
        return
    rec(idx + 1, int(bin(val | ls[idx][1]), 2), cnt + 1)
    rec(idx + 1, val, cnt)

rec(0, 0, 0)
res.sort(key = lambda x : (-x[0], x[1]))
print(res[0][1] if len(res) != 0 else -1)
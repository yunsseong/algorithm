n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
gom = list(map(int, input().split()))
minn = int(1e9)

def rec(idx, r, g, b, cnt):
    global n, minn
    if idx == n:
        if 2 <= cnt <= 7:
            r = r // cnt if r != 0 else 0
            g = g // cnt if g != 0 else 0
            b = b // cnt if b != 0 else 0
            minn = min(minn, abs(r - gom[0]) + abs(g - gom[1]) + abs(b - gom[2]))
        return

    if cnt > 7:
        return
    rec(idx + 1, r + ls[idx][0], g + ls[idx][1], b + ls[idx][2], cnt + 1)
    rec(idx + 1, r, g, b, cnt)

rec(0, 0, 0, 0, 0)
print(minn)

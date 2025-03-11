def rec(idx, difficulty, easiest, hardiest, cnt):
    global n, l, r, x, a, res
    if idx == len(a):
        if cnt >= 2 and difficulty >= l and difficulty <= r and hardiest - easiest >= x:
            res += 1
            return
        else:
            return

    rec(idx + 1, difficulty + a[idx], min(easiest, a[idx]), max(hardiest, a[idx]), cnt + 1)
    rec(idx + 1, difficulty, easiest, hardiest, cnt)

n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))
res = 0
rec(0, 0, 1000000, 1, 0)
print(res)



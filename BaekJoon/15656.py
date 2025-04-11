n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

selected = [0] * m
def rec(cur):
    if cur == m:
        print(*selected)
        return

    for i in range(n):
        selected[cur] = nums[i]
        rec(cur + 1)
rec(0)
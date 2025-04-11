n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

selected = [0] * m
visited = [False] * n

def rec(cur, start):
    if cur == m:
        print(*selected)
        return

    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        selected[cur] = nums[i]
        rec(cur + 1, i + 1)
        visited[i] = False
rec(0, 0)
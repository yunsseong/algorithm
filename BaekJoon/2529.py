n = int(input())
ls = list(input().split())

selected = [0] * (n + 1)
visited = [False] * 10
res = []
def rec(cur):
    if cur == n + 1:
        flag = True
        for i in range(n):
            if ls[i] == "<":
                if selected[i] >= selected[i + 1]:
                    flag = False
                    break
            if ls[i] == ">":
                if selected[i] <= selected[i + 1]:
                    flag = False
                    break
        if flag:
            res.append(''.join(map(str, selected)))
        return

    for i in range(10):
        if visited[i]:
            continue
        visited[i] = True
        selected[cur] = i
        rec(cur + 1)
        visited[i] = False
rec(0)
print(res[-1])
print(res[0])

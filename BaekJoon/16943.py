a, b = map(int, input().split())
a = list(str(a))
selected = [0] * len(a)
visited = [False] * len(a)
res = -1
def rec(cur):
    global a, b, selected, visited, res
    if cur == len(a):
        c = int(''.join(map(str, selected)))
        if selected[0] != 0 and c < b:
            res = max(res, c)

    for i in range(len(a)):
        if visited[i]:
            continue
        visited[i] = True
        selected[cur] = int(a[i])
        rec(cur + 1)
        visited[i] = False
rec(0)
print(res)
from collections import deque

s = int(input())
d = deque()
d.append([1, 0, 0])
minn = 3 * 1000
visited = [False] * 1001

while d:
    cur, clip, cnt = d.popleft()
    if cur == s:
        print(cnt)
        break

    if 0 < cur < 1001 and not visited[cur]:
        visited[cur] = True
        d.append([cur, cur, cnt + 1])
    if 0 < cur + clip < 1001 and clip > 0:
        d.append([cur + clip, clip, cnt + 1])
    if 0 < cur - 1 < 1001 and not visited[cur - 1]:
        d.append([cur - 1, clip, cnt + 1])

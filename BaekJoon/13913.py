from collections import deque

n, k = map(int, input().split())
d = deque()
d.append([n, [str(n)]])
visited = [False] * 100001

if n > k:
    print(n - k)
    print(' '.join([str(i) for i in range(n, k-1, -1)]))
else:
    while d:
        cur, trace = d.popleft()
        if cur == k:
            print(len(trace)-1)
            print(' '.join(map(str, trace)))
            break

        for i in [cur, -1, 1]:
            nx = cur + i
            if 0 <= nx < 100001 and not visited[nx]:
                visited[nx] = True
                d.append([nx, trace + [str(nx)]])

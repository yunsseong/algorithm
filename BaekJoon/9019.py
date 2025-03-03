from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    q = deque()
    a, b = map(int, input().split())
    q.append([a, ''])
    visited = [False for _ in range(10001)]
    visited[a] = True
    while q:
        cur, cmd = q.popleft()
        if cur == b:
            print(cmd)
            break

        for i in ["D", "S", "L", "R"]:
            if i == "D":
                nx = (cur * 2) % 10000
                if not visited[nx]:
                    visited[nx] = True
                    q.append([nx, cmd + i])
                continue

            if i == "S":
                nx = cur - 1 if cur > 0 else 9999
                if not visited[nx]:
                    visited[nx] = True
                    q.append([nx, cmd + i])
                continue

            if i == "L":
                nx = cur // 1000 + cur % 1000 * 10
                if not visited[nx]:
                    visited[nx] = True
                    q.append([nx, cmd + i])
                continue

            if i == "R":
                nx = cur // 10 + cur % 10 * 1000
                if not visited[nx]:
                    visited[nx] = True
                    q.append([nx, cmd + i])
                continue




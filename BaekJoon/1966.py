from collections import deque

n = int(input())

for _ in range(n):
    n, m = map(int, input().split())
    papers = list(map(int, input().split()))
    queue = deque([[x, i] for i, x in enumerate(papers)])

    cnt = 0

    while queue:
        if queue[0] == max(queue, key = lambda x : x[0]):
            cnt += 1
            if queue[0][1] == m:
                print(cnt)
                break
            queue.popleft()
        else:
            queue.append(queue.popleft())









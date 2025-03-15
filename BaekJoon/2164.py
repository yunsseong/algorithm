import sys
from collections import deque

n = int(input())
nums = [i for i in range(1, n + 1)]
q = deque()
q.extend(nums)

if n == 1:
    print(1)
    sys.exit()

while len(q) != 1:
    q.popleft()
    if len(q) > 1:
        q.append(q.popleft())
    else:
        print(q[0])

